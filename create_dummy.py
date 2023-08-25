import csv
import os
import random
import openpyxl

from faker import Faker
from tabulate import tabulate
from datetime import datetime, timedelta

fake = Faker("id_ID")


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


def xlsx_to_dict(file_path, sheet_name):
    """
    Convert an XLSX file to a dictionary using openpyxl.

    Args:
        file_path (str): Path to the XLSX file.
        sheet_name (str): Name of the sheet in the XLSX file.

    Returns:
        dict: A dictionary containing the data from the specified sheet.
    """
    data_dict = {}

    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)

    try:
        # Get the specified sheet
        sheet = workbook[sheet_name]

        # Iterate through rows, excluding the header row
        for row in sheet.iter_rows(min_row=2, values_only=True):
            kota_id, nama_kota, latitude, longitude = row
            kota_id = int(kota_id)
            data_dict[kota_id] = {
                "nama_kota": nama_kota,
                "latitude": latitude,
                "longitude": longitude,
            }
    except KeyError:
        print(f"Sheet '{sheet_name}' not found in the workbook.")

    return data_dict


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
        manufacture_id = f"M-{id_format}"  # Create a formatted manufacturing
        manufactures.append(
            (manufacture_id, manufacture)
        )  # Add (manufacture_id, manufacture) to the list

    if is_printed:
        show_table(manufactures, ["manufacture_id", "manufacture_name"])

    return manufactures


# Function to generate car models with optional printing
def generate_car_models(
    data: dict, manufactures_table: list, is_printed: bool = True
) -> list:
    """Generate a table of car models with formatted IDs.

    Args:
        data (dict): A dictionary containing car data with body types as keys.
        manufactures_table (list): A list of manufacturers' data.
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
                for manufacture in manufactures_table
                if manufacture[1] == manufacture_name
            )

            car_model_count += 1
            car_model_id = f"CM{car_model_count:04}"

            car_models.append((car_model_id, manufacture_id, model))

    sorted_car_models = sorted(car_models, key=lambda x: x[0])  # Sort car models by ID

    if is_printed:
        show_table(sorted_car_models, ["model_id", "manufacture_id", "model_name"])

    return sorted_car_models


def generate_cars(
    data: dict,
    manufactures_table: list,
    body_types_table: list,
    car_models_table: list,
    n_data: int,
    is_printed: bool = True,
) -> list:
    """
    Generate dummy car data based on specified parameters.

    Args:
        data (dict): A dictionary containing car data
                     with body types as keys.
        manufactures_table (list): A list of manufacturers' data.
        body_types_table (list): A list of body types data.
        car_models_table (list): A list of car models data.
        n_data (int): The number of dummy data to generate.
        is_printed (bool, optional): Whether to print the generated data.
                                     Defaults to True.

    Returns:
        list: A list of tuples containing generated car data.
    """
    dummy_data = []

    body_types = [body_type for body_type in data.keys()]

    car_id_counter = 1  # Initialize the car_id counter

    for _ in range(n_data):
        car_id = car_id_counter  # Set the car_id using the counter value
        car_id_counter += 1  # Increment the car_id counter

        # Select a random body type and model name
        body_type = random.choice(body_types)
        model_name = random.choice(list(data[body_type].keys()))

        # Extract necessary information from car data
        manufacture_name = data[body_type][model_name]["pabrikan"]
        manufacture_id = next(
            manufacture[0]
            for manufacture in manufactures_table
            if manufacture[1] == manufacture_name
        )

        year_data = data[body_type][model_name]["tahun"]
        if year_data:  # Make sure there are valid years for the model
            year_index = random.randint(0, len(year_data) - 1)
            year_manufactured = year_data[year_index]
        else:
            year_manufactured = None  # Set a default year if no year data

        engine_capacity = data[body_type][model_name]["kapasitas_mesin"]

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
        model_id = next(
            model[0] for model in car_models_table if model[2] == model_name
        )
        body_type_id = next(
            body[0] for body in body_types_table if body[1] == body_type
        )

        # Append generated car data to dummy_data list
        dummy_data.append(
            (
                car_id,
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
            "car_id",
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


def generate_locations(data: dict, is_printed: bool = True) -> list:
    """
    Generate a list of location data from a dictionary.

    Args:
        data (dict): A dictionary containing location data.
        is_printed (bool, optional): Whether to print the generated data.
                                     Defaults to True.

    Returns:
        list: A list of tuples containing location data.
              Each tuple has the format: (
                            location_id,
                            city_name,
                            (latitude, longitude)
                        ).
    """

    location_list = []  # Initialize an empty list to store location data

    # Iterate through the items in the 'data' dictionary
    for id, lokasi in data.items():
        # Create a tuple containing location data and append it to the list
        # Each tuple contains the location ID, city name,
        # and a tuple of latitude and longitude
        location_list.append(
            (id, lokasi["nama_kota"], (lokasi["latitude"], lokasi["longitude"]))
        )

    # Check if 'is_printed' is True
    if is_printed:
        # If True, display the location data in a table using
        # the 'show_table' function
        show_table(location_list, ["location_id", "city_name", "location"])

    # Return the list of location data
    return location_list


def generate_name(n_names):
    """
    Generate dummy names.

    Args:
        n_names (int): The number of dummy names to generate.

    Returns:
        list: A list of generated names.
    """
    names = []  # Initialize an empty list to store generated names

    # Loop until the desired number of names is generated
    while len(names) < n_names:
        # Generate a random first name and last name using Faker library
        first_name = fake.first_name()
        last_name = fake.last_name()

        # Combine the first name and last name to create a full name
        full_name = f"{first_name} {last_name}"

        # Check if the full name is not already in the list of names
        if full_name not in names:
            # If not, add the full name to the list
            names.append(full_name)

    # Return the list of generated names
    return names


# Generate customer data
def generate_customer(
    location_table: list, n_data: int, is_printed: bool = True
) -> list:
    """Generate dummy customer data based on specified parameters.

    Args:
        location_table (list): A list of location data.
    n_data (int): The number of dummy data to generate.
    is_printed (bool, optional): Whether to print the generated data. Defaults to True.

    Returns:
    list: A list of tuples containing generated customer data.
    """
    customer_data = []  # Initialize an empty list to store customer data

    user_id = 0

    data = generate_name(n_data)  # Generate a list of dummy names

    # Iterate through the list of generated names
    for name in data:
        user_id += 1
        # Split the full name into first name and last name
        first_name = name.split(" ")[0]
        last_name = name.split(" ")[1]

        # Generate email using the full name and Faker's free email domain
        email = f"{name.lower().replace(' ','.')}@{fake.free_email_domain()}"

        # Generate a fake phone number
        contact = fake.phone_number()

        # Choose a random location ID from the list of location data
        location_id = random.choice([id[0] for id in location_table])

        # Create a tuple containing customer data and append it to the list
        customer_data.append(
            (user_id, first_name, last_name, email, contact, location_id)
        )

    # Check if 'is_printed' is True
    if is_printed:
        # If True, display the customer data in a table using
        # the 'show_table' function
        header = [
            "user_id",
            "first_name",
            "last_name",
            "email",
            "contact",
            "location_id",
        ]
        show_table(customer_data, header)

    # Return the list of customer data
    return customer_data


def generate_ad_title():
    """
    Generate a random advertisement title using a combination of keywords.

    Returns:
        str: A randomly generated advertisement title.
    """
    # List of keywords
    keywords = [
        "Bekas",
        "Tahun",
        "Km",
        "Kondisi",
        "Mulus",
        "Service",
        "Baru",
        "Jarang",
        "Terawat",
        "Mesin",
        "Interior",
        "Eksterior",
        "Full",
        "Original",
        "Pajak",
        "Surat",
        "Siap",
        "Oli",
        "Ban",
        "Velg",
        "Warna",
        "Cat",
        "Jual",
        "Murah",
        "Harga",
        "Cash",
        "Kredit",
        "DP",
        "Cicilan",
        "Negotiable",
        "Nego",
        "Asli",
        "Mobil",
        "Berkualitas",
        "Pakai",
        "Langsung",
        "Terjamin",
        "Dokumen",
        "Tangan",
        "Jarak",
        "Kendaraan",
        "Pemakaian",
        "Pribadi",
        "Bukan Rental",
        "Nopol",
        "Kilometer",
        "STNK",
    ]

    # Randomly choose keywords to create a title
    num_keywords = random.randint(5, 10)  # Choose 5 to 10 keywords
    selected_keywords = random.sample(keywords, num_keywords)

    # Capitalize the first letter of each keyword and join them to form a title
    title = " ".join([keyword.capitalize() for keyword in selected_keywords])

    return title


def generate_advertisement(
    data: dict,
    customer_table: list,
    cars_table: list,
    car_models_table: list,
    n_data: int,
    is_printed: bool = True,
) -> list:
    """
    Generate dummy advertisement data based on specified parameters.

    Args:
        data (dict) : A dictionary containing car data
                      with body types as keys.
        customer_table (list): A list of customer data.
        cars_table (list): A list of cars data.
        car_models_table (list): A list of car models data.
        n_data (int): The number of dummy advertisement data to generate.
        is_printed (bool, optional): Whether to print the generated data.
                                     Defaults to True.

    Returns:
        list: A list of tuples containing generated advertisement data.
    """
    ad_list = []

    ad_id_counter = 1

    for _ in range(n_data):
        # Randomly select user_id from customer_data
        user_id = random.choice([id[0] for id in customer_table])

        # Generate a random ad title using the generate_ad_title function
        title = generate_ad_title()

        # Generate a random ad description using faker's paragraph function
        description = fake.paragraph()

        # Randomly select car_id and car_model_id from cars_data
        car_id, car_model_id = random.choice([(id[0], id[2]) for id in cars_table])

        try:
            # Find the index of the car model in car_models_data
            # based on car_model_id
            index = next(
                index
                for index, tuple_value in enumerate(car_models_table)
                if car_model_id in tuple_value
            )
            model_name = car_models_table[index][2]

            price = None  # Initialize price variable

            # Iterate through car_data to find matching model name and
            # retrieve price
            for body_type in data.keys():
                for model, details in data[body_type].items():
                    if model == model_name:
                        # If price is a list, randomly choose a price from the list
                        if isinstance(details["harga"], list):
                            price = random.choice(details["harga"])
                        else:
                            # If price is an integer, set the price directly
                            price = details["harga"]
                        break  # Exit the loop after finding the price

            if price is None:
                print(f"Price not found for model: {model_name}")
                continue

        except StopIteration:
            print(f"Car model ID {car_model_id} not found in the list")
            continue

        # Generate a random date within the current year for date_posted
        date_posted = fake.date_time_this_year() - timedelta(
            days=random.randint(0, 150)
        )

        if isinstance(price, list):
            selected_price = random.choice(price)
        else:
            selected_price = price

        # Append the generated ad data to ad_list
        ad_list.append(
            (
                ad_id_counter,
                user_id,
                title,
                selected_price,
                description,
                car_id,
                date_posted,
            )
        )
        ad_id_counter += 1

    if is_printed:
        # Display the generated ad data in a table
        show_table(
            ad_list,
            [
                "ad_id",
                "user_id",
                "title",
                "price",
                "description",
                "car_id",
                "date_posted",
            ],
        )

    return ad_list


def generate_bids(
    advertisement_table: list,
    customer_table: list,
    n_data: int,
    is_printed: bool = True,
) -> list:
    """
    Generate dummy bid data based on specified parameters.

    Args:
        advertisement_table (list): A list of advertisement data.
        customer_table (list): A list of customer data.
        n_data (int): The number of dummy bid data to generate.
        is_printed (bool, optional): Whether to print the generated data.
                                     Defaults to True.

    Returns:
        list: A list of tuples containing generated bid data.
    """
    bid_list = []

    for _ in range(n_data):
        # Randomly select an advertisement
        ad_id, user, price, date_posted = random.choice(
            [(id[0], id[1], id[3], id[6]) for id in advertisement_table]
        )

        # Randomly select a user_id for bidding (excluding the original ad
        user_id = random.choice([id[0] for id in customer_table if id[0] != user])

        # Calculate low and high bid prices based on the ad price
        low_price = int(0.8 * price)
        high_price = int(0.95 * price)

        # Generate a random bid price within the calculated range
        bid_price = fake.random_int(low_price, high_price, 1_500_000)

        # Randomly choose bid_status with weights
        # (70% for 'rejected', 30% for 'approved')
        bid_status = random.choices(["approved", "rejected"], weights=(0.3, 0.7))[0]

        # Generate a random datetime for bidding  after ad's date_posted
        datetime_bid = date_posted + timedelta(days=random.randint(1, 7))

        # Append the generated bid data to bid_list
        bid_list.append((ad_id, user_id, bid_price, bid_status, datetime_bid))

    if is_printed:
        # Display the generated bid data in a table
        show_table(
            bid_list, ["ad_id", "user_id", "bid_price", "bid_status", "datetime_bid"]
        )

    return bid_list
