import csv
import os
import random

from faker import Faker
from tabulate import tabulate

fake = Faker()


# Function to display a table using tabulate
def show_table(data_list: list, headers: list):
    """
    Display a table using tabulate.

    Args:
        data_list (list): The list of data to be displayed.
        headers (list): The list of header names for the table.
    """
    table = tabulate(data_list, headers=headers, tablefmt="pretty")
    print(table)


# Function to export list to a CSV file
def list_to_csv(data_list: list, folder_path: str, filename: str, headers: list):
    """
    Export data from a list to a CSV file.

    Args:
        data_list (list): The list containing data to be exported.
        folder_path (str): The path to the folder where the CSV file will
                           be saved.
        filename (str): The name of the CSV file.
        headers (list): A list of header names for the CSV file.
    """
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, filename)

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write headers
        writer.writerow(headers)

        # Write data
        for row in data_list:
            writer.writerow(row)


# Function to generate body types with optional printing
def generate_body_types(data: dict, is_printed: bool = True) -> list:
    """Generate a list of body types with formatted manufacturing IDs.

    Args:
        data (dict): A dictionary containing car data with body types as keys.
        is_printed (bool, optional): Whether to print the table.
                                     Defaults to True.

    Returns:
        list: A list of tuples containing formatted manufacturing IDs and
              body types.
    """
    body_types = []  # Initialize an empty list to store the result pairs
    for id, body in enumerate(sorted(data.keys()), start=1):
        id_format = f"{id:03}"  # Format the index to three digits
        body_type_id = f"BT-{id_format}"  # Create a formatted body type ID
        body_types.append(
            (body_type_id, body)
        )  # Add (body_type_id, body) pair to the list

    if is_printed:
        show_table(body_types, ["body_type_id", "body_type_name"])

    return body_types


# Function to generate manufacturers with optional printing
def generate_manufactures(data: dict, is_printed: bool = True) -> list:
    """Generate a table of manufacturers with formatted IDs.

    Args:
        data (dict): A dictionary containing car data with manufacturers'
                     information.
        is_printed (bool, optional): Whether to print the table.
                                     Defaults to True.

    Returns:
        list: A list of tuples containing formatted manufacturing IDs and
              manufacturer names.
    """
    manufacturer_set = set()  # Initialize a set to store unique manufacturers
    for body_type in data.keys():
        for model, details in data[body_type].items():
            manufacturer_set.add(details["pabrikan"])  # Unique value

    manufactures = []  # Initialize a list to store the result tuples
    for id, manufacture in enumerate(sorted(manufacturer_set), start=1):
        id_format = f"{id:02}"  # Format the index to two digits
        manufacture_id = f"M-{id_format}"  # Create a formatted manufacturing ID
        manufactures.append(
            (manufacture_id, manufacture)
        )  # Add (manufacture_id, manufacture) to the list

    if is_printed:
        show_table(manufactures, ["manufacture_id", "manufacture_name"])

    return manufactures


# Function to generate car models with optional printing
def generate_car_models(
    data: dict, manufactures_data: list, is_printed: bool = True
) -> list:
    """Generate a table of car models with formatted IDs.

    Args:
        data (dict): A dictionary containing car data with body types as keys.
        manufactures_data (list): A list of manufacturers' data.
        is_printed (bool, optional): Whether to print the table.
                                     Defaults to True.

    Returns:
        list: A list of tuples containing formatted car model IDs,
              manufacturing IDs, and model names.
    """
    car_models = []  # Initialize a list to store the result tuples
    car_model_count = 0  # Initialize a counter for car models

    for body_type in data.keys():
        for model, details in data[body_type].items():
            manufacture_name = details["pabrikan"]
            manufacture_id = next(
                manufacture[0]
                for manufacture in manufactures_data
                if manufacture[1] == manufacture_name
            )

            car_model_count += 1
            car_model_id = f"CM{car_model_count:04}"

            car_models.append((car_model_id, manufacture_id, model))

    sorted_car_models = sorted(car_models, key=lambda x: x[0])

    if is_printed:
        show_table(sorted_car_models, ["car_model_id", "manufacture_id", "model_name"])

    return sorted_car_models


def generate_cars(
    car_data: dict,
    manufactures_data: list,
    body_types_data: list,
    car_models_data: list,
    n_data: int,
    is_printed: bool = True,
) -> list:
    """
    Generate dummy car data based on specified parameters.

    Args:
        car_data (dict): A dictionary containing car data with
                         body types as keys.
        manufactures_data (list): A list of manufacturers' data.
        body_types_data (list): A list of body types data.
        car_models_data (list): A list of car models data.
        n_data (int): The number of dummy data to generate.
        is_printed (bool, optional): Whether to print the generated data.
                                     Defaults to True.

    Returns:
        list: A list of tuples containing generated car data.
    """
    dummy_data = []

    body_types = [body_type for body_type in car_data.keys()]

    for _ in range(n_data):
        # Select a random body type and model name
        body_type = random.choice(body_types)
        model_name = random.choice(list(car_data[body_type].keys()))

        # Extract necessary information from car data
        manufacture_name = car_data[body_type][model_name]["pabrikan"]
        manufacture_id = next(
            manufacture[0]
            for manufacture in manufactures_data
            if manufacture[1] == manufacture_name
        )

        year_data = car_data[body_type][model_name]["tahun"]
        if year_data:  # Make sure there are valid years for the model
            year_index = random.randint(0, len(year_data) - 1)
            year_manufactured = year_data[year_index]
        else:
            year_manufactured = None  # Set a default year if no year data

        engine_capacity = car_data[body_type][model_name]["kapasitas_mesin"]

        # Determine passenger capacity based on body type
        passenger_capacity = None  # Initialize passenger_capacity
        if body_type == "MPV":
            passenger_capacity = 7
        elif body_type in [
            "LCGC",
            "Hybrid",
            "Elektrik",
            "Double Cabin",
            "Station Wagon",
            "Sedan",
            "Hatchback",
            "SUV",
            "Crossover",
        ]:
            passenger_capacity = 5
        elif body_type in ["Offroad", "Sport"]:
            passenger_capacity = 4
        elif body_type == "Convertible":
            passenger_capacity = 2

        # Determine transmission type based on body type
        transmission_types = ["manual", "automatic"]
        if body_type in ["Hybrid", "Elektrik"]:
            transmission_type = "automatic"
        else:
            transmission_type = random.choice(transmission_types)

        # Determine fuel type based on body type
        fuel_types = ["gasoline", "diesel"]
        if body_type == "Hybrid":
            fuel_type = "hybrid"
        elif body_type == "Elektrik":
            fuel_type = "electric"
        else:
            fuel_type = random.choice(fuel_types)

        # Determine drive system based on body type
        drive_systems = ["RWD", "AWD"]
        if body_type == "Offroad":
            drive_system = "FWD"
        else:
            drive_system = random.choice(drive_systems)

        # Generate random odometer and additional details
        odometer = fake.random_int(min=100, max=150000)
        additional_details = fake.paragraph()

        # Retrieve model and body type IDs from the respective data lists
        model_id = next(model[0] for model in car_models_data if model[2] == model_name)
        body_type_id = next(body[0] for body in body_types_data if body[1] == body_type)

        # Append generated car data to dummy_data list
        dummy_data.append(
            (
                manufacture_id,
                model_id,
                body_type_id,
                year_manufactured,
                engine_capacity,
                passenger_capacity,
                transmission_type,
                fuel_type,
                drive_system,
                odometer,
                additional_details,
            )
        )

    # Display the generated data if is_printed is True
    if is_printed:
        header = [
            "manufacture_id",
            "model_id",
            "body_type_id",
            "year_manufactured",
            "engine_capacity",
            "passenger_capacity",
            "transmission_type",
            "fuel_type",
            "drive_system",
            "odometer",
            "additional_details",
        ]
        show_table(dummy_data, header)

    return dummy_data
