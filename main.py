from create_dummy import (
    list_to_csv,
    xlsx_to_dict,
    generate_body_types,
    generate_manufactures,
    generate_car_models,
    generate_cars,
    generate_locations,
    generate_customer,
    generate_advertisement,
    generate_bids,
)

car_data = {
    "SUV": {
        "Honda HR-V": {
            "pabrikan": "Honda",
            "tahun": [2016, 2018, 2019],
            "harga": [210_000_000, 245_000_000, 265_000_000],
            "kapasitas_mesin": 1.5,
        },
        "Toyota Rush": {
            "pabrikan": "Toyota",
            "tahun": [2021, 2022, 2023],
            "harga": [228_000_000, 254_000_000, 276_000_000],
            "kapasitas_mesin": 1.5,
        },
        "Daihatsu Terios": {
            "pabrikan": "Daihatsu",
            "tahun": [2013, 2016, 2018],
            "harga": [120_000_000, 167_000_000, 197_000_000],
            "kapasitas_mesin": 1.5,
        },
        "Toyota Fortuner": {
            "pabrikan": "Toyota",
            "tahun": [2017, 2019, 2021],
            "harga": [285_000_000, 463_000_000, 520_000_000],
            "kapasitas_mesin": 2.4,
        },
        "Suzuki Ignis": {
            "pabrikan": "Suzuki",
            "tahun": [2018, 2019, 2020],
            "harga": [130_000_000, 139_000_000, 155_000_000],
            "kapasitas_mesin": 1.2,
        },
    },
    "MPV": {
        "Toyota Avanza": {
            "pabrikan": "Toyota",
            "tahun": [2014, 2015, 2016],
            "harga": [130_000_000, 135_000_000, 155_000_000],
            "kapasitas_mesin": 1.5,
        },
        "Honda Mobilio": {
            "pabrikan": "Honda",
            "tahun": [2015, 2018, 2020],
            "harga": [146_000_000, 181_000_000, 212_500_000],
            "kapasitas_mesin": 1.5,
        },
        "Wuling Confero": {
            "pabrikan": "Wuling",
            "tahun": [2019],
            "harga": 155_000_000,
            "kapasitas_mesin": 1.5,
        },
        "Toyota Sienta": {
            "pabrikan": "Toyota",
            "tahun": [2017, 2019, 2021],
            "harga": [180_000_000, 195_000_000, 230_000_000],
            "kapasitas_mesin": 1.5,
        },
    },
    "Crossover": {
        "Mitsubishi Xpander Cross": {
            "pabrikan": "Mitsubishi",
            "tahun": [2019, 2020, 2021],
            "harga": [215_000_000, 230_000_000, 276_000_000],
            "kapasitas_mesin": 1.5,
        },
        "Nissan Juke": {
            "pabrikan": "Nissan",
            "tahun": [2011, 2013, 2015],
            "harga": [125_000_000, 130_000_000, 135_000_000],
            "kapasitas_mesin": 1.5,
        },
        "Mazda CX-3": {
            "pabrikan": "Mazda",
            "tahun": [2017, 2018, 2019],
            "harga": [265_000_000, 285_000_000, 300_000_000],
            "kapasitas_mesin": 2.0,
        },
    },
    "Hatchback": {
        "Honda Brio": {
            "pabrikan": "Honda",
            "tahun": [2014, 2016, 2018],
            "harga": [125_000_000, 135_000_000, 155_000_000],
            "kapasitas_mesin": 1.2,
        },
        "Suzuki Baleno GL": {
            "pabrikan": "Suzuki",
            "tahun": [2017, 2018, 2019],
            "harga": [154_000_000, 185_000_000, 199_000_000],
            "kapasitas_mesin": 1.4,
        },
        "Toyota Yaris": {
            "pabrikan": "Toyota",
            "tahun": [2013, 2015, 2017],
            "harga": [130_000_000, 150_000_000, 190_000_000],
            "kapasitas_mesin": 1.5,
        },
        "Mazda 2": {
            "pabrikan": "Mazda",
            "tahun": [2017, 2018, 2019],
            "harga": [205_000_000, 230_000_000, 235_000_000],
            "kapasitas_mesin": 1.5,
        },
        "Honda Jazz": {
            "pabrikan": "Honda",
            "tahun": [2006, 2007, 2008],
            "harga": [95_000, 107_000_000, 112_000],
            "kapasitas_mesin": 1.5,
        },
    },
    "Sedan": {
        "Toyota Corolla Altis": {
            "pabrikan": "Toyota",
            "tahun": [2012, 2015, 2018],
            "harga": [110_000_000, 215_000_000, 260_000_000],
            "kapasitas_mesin": 1.8,
        },
        "Toyota Vios": {
            "pabrikan": "Toyota",
            "tahun": [2015, 2018, 2021],
            "harga": [130_000_000, 200_000_000, 225_000_000],
            "kapasitas_mesin": 1.4,
        },
        "Toyota Camry": {
            "pabrikan": "Toyota",
            "tahun": [2013, 2015, 2017],
            "harga": [200_000_000, 230_000_000, 300_000_000],
            "kapasitas_mesin": 2.5,
        },
        "Mazda 6": {
            "pabrikan": "Mazda",
            "tahun": [2013, 2014, 2017],
            "harga": [230_000_000, 260_000_000, 350_000_000],
            "kapasitas_mesin": 2.5,
        },
    },
    "Sport": {
        "Honda Civic Type-R": {
            "pabrikan": "Honda",
            "tahun": [2017, 2018, 2019],
            "harga": [850_000_000, 910_000_000, 1_100_000_000],
            "kapasitas_mesin": 2.0,
        },
        "BMW Series 3": {
            "pabrikan": "BMW",
            "tahun": [2016, 2018, 2020],
            "harga": [450_000_000, 600_000_000, 850_000_000],
            "kapasitas_mesin": 3.0,
        },
        "Mercedes-Benz C-Class": {
            "pabrikan": "Mercedes",
            "tahun": [2015, 2017, 2019],
            "harga": [550_000_000, 600_000_000, 650_000_000],
            "kapasitas_mesin": 4.0,
        },
        "Audi A5": {
            "pabrikan": "Audi",
            "tahun": [2013, 2014, 2023],
            "harga": [485_000_000, 550_000_000, 1_425_000_000],
            "kapasitas_mesin": 3.0,
        },
    },
    "Convertible": {
        "Porsche 718": {
            "pabrikan": "Porsche",
            "tahun": [2017, 2018, 2021],
            "harga": [2_150_000_000, 2_190_000_000, 2_575_000_000],
            "kapasitas_mesin": 2.0,
        },
        "BMW Z4": {
            "pabrikan": "BMW",
            "tahun": [2015, 2019, 2021],
            "harga": [819_000_000, 1_295_000_000, 1_625_000_000],
            "kapasitas_mesin": 3.0,
        },
        "Mazda MX-5": {
            "pabrikan": "Mazda",
            "tahun": [2012, 2018, 2020],
            "harga": [253_000_000, 645_000_000, 675_000_000],
            "kapasitas_mesin": 2.0,
        },
        "Mini Cabrio John Cooper Works": {
            "pabrikan": "Mini",
            "tahun": [2012, 2016, 2019],
            "harga": [545_000_000, 625_000, 895_000_000],
            "kapasitas_mesin": 2.0,
        },
        "Mercedes-Benz SLK-Class": {
            "pabrikan": "Mercedes",
            "tahun": [2006, 2010, 2012],
            "harga": [450_000_000, 517_000_000, 800_000_000],
            "kapasitas_mesin": 3.5,
        },
    },
    "Station Wagon": {
        "Mini Clubman Cooper S": {
            "pabrikan": "Mini",
            "tahun": [2016, 2019, 2020],
            "harga": [675_000_000, 905_000_000, 975_000_000],
            "kapasitas_mesin": 2.0,
        },
        "Volkswagen Golf": {
            "pabrikan": "Volkswagen",
            "tahun": [2020, 2022, 2023],
            "harga": [1_500_000_000, 1_700_000_000, 1_950_000_000],
            "kapasitas_mesin": 2.0,
        },
        "Mercedes-Benz GLE-Class": {
            "pabrikan": "Mercedes",
            "tahun": [2019, 2020, 2021],
            "harga": [1_450_000_000, 1_745_000_000, 1_845_000_000],
            "kapasitas_mesin": 3.0,
        },
    },
    "Offroad": {
        "Suzuki Jimny": {
            "pabrikan": "Suzuki",
            "tahun": [2017, 2019, 2021],
            "harga": [380_000_000, 450_000_000, 510_000_000],
            "kapasitas_mesin": 1.5,
        },
        "Jeep Wrangler Sahara": {
            "pabrikan": "Jeep",
            "tahun": [2013, 2014, 2023],
            "harga": [860_000_000, 899_000_000, 1_980_000_000],
            "kapasitas_mesin": 3.6,
        },
        "Land Rover Defender": {
            "pabrikan": "Land Rover",
            "tahun": [2013, 2014, 2016],
            "harga": [1_350_000_000, 1_750_000_000, 2_550_000_000],
            "kapasitas_mesin": 2.2,
        },
        "Mercedes-Benz G63 AMG": {
            "pabrikan": "Mercedes",
            "tahun": [2013, 2016, 2019],
            "harga": [4_000_000_000, 4_650_000_000, 5_800_000_000],
            "kapasitas_mesin": 5.5,
        },
    },
    "Double Cabin": {
        "Toyota Hilux G": {
            "pabrikan": "Toyota",
            "tahun": [2012, 2014, 2023],
            "harga": [245_000_000, 325_000_000, 440_000_000],
            "kapasitas_mesin": 2.5,
        },
        "Ford Ranger XLT": {
            "pabrikan": "Ford",
            "tahun": [2012, 2015, 2022],
            "harga": [297_000_000, 445_000_000, 590_000_000],
            "kapasitas_mesin": 2.2,
        },
        "Mitsubishi Triton Exceed": {
            "pabrikan": "Mitsubishi",
            "tahun": [2016, 2018, 2022],
            "harga": [365_000_000, 398_000_000, 470_000_000],
            "kapasitas_mesin": 2.5,
        },
    },
    "Elektrik": {
        "Tesla Model 3": {
            "pabrikan": "Tesla",
            "tahun": [2020, 2021, 2022],
            "harga": [975_000_000, 1_075_000_000, 1_650_000_000],
            "kapasitas_mesin": 0,
        },
        "Hyundai IONIQ 5": {
            "pabrikan": "Hyundai",
            "tahun": [2021, 2022, 2023],
            "harga": [679_000_000, 775_000_000, 825_000_000],
            "kapasitas_mesin": 0,
        },
        "Wuling Air EV": {
            "pabrikan": "Wuling",
            "tahun": [2021, 2022, 2023],
            "harga": [230_000_000, 245_000_000, 300_000_000],
            "kapasitas_mesin": 0,
        },
    },
    "Hybrid": {
        "Nissan Kicks": {
            "pabrikan": "Nissan",
            "tahun": [2020, 2021, 2023],
            "harga": [320_000_000, 375_000_000, 500_000_000],
            "kapasitas_mesin": 1.2,
        },
        "Toyota Camry Hybrid": {
            "pabrikan": "Toyota",
            "tahun": [2013, 2014, 2017],
            "harga": [220_000_000, 275_0000_000, 355_000_000],
            "kapasitas_mesin": 2.5,
        },
        "Suzuki Ertiga GX Hybrid": {
            "pabrikan": "Suzuki",
            "tahun": [2021, 2022, 2023],
            "harga": [200_000_000, 225_000_000, 242_000_000],
            "kapasitas_mesin": 1.5,
        },
    },
    "LCGC": {
        "Toyota Calya": {
            "pabrikan": "Toyota",
            "tahun": [2016, 2019, 2022],
            "harga": [110_000_000, 127_000_000, 147_500_000],
            "kapasitas_mesin": 1.2,
        },
        "Daihatsu Sigra": {
            "pabrikan": "Daihatsu",
            "tahun": [2017, 2019, 2021],
            "harga": [100_000_000, 123_000_000, 159_000_000],
            "kapasitas_mesin": 1.2,
        },
    },
}

# Call the function and store the result
body_type_data = generate_body_types(data=car_data, is_printed=False)

# Generate manufacturers data
manufactures_data = generate_manufactures(data=car_data, is_printed=False)

# Generate and sort car models data
car_models_data = generate_car_models(
    data=car_data, manufactures_table=manufactures_data, is_printed=False
)

# Generate cars data
cars_table_data = generate_cars(
    data=car_data,
    manufactures_table=manufactures_data,
    body_types_table=body_type_data,
    car_models_table=car_models_data,
    n_data=200,
    is_printed=False,
)

# Load data from XLSX file and generate location data
xlsx_file_path = "city.xlsx"
sheet_name = "city"
location_data = generate_locations(
    data=xlsx_to_dict(xlsx_file_path, sheet_name=sheet_name), is_printed=False
)

# Generate customer data
customer_data = generate_customer(
    location_table=location_data, n_data=400, is_printed=False
)

# generate_advertisement function with the required parameters
advertisement_data = generate_advertisement(
    data=car_data,
    customer_table=customer_data,
    cars_table=cars_table_data,
    car_models_table=car_models_data,
    n_data=500,
    is_printed=False,
)

# Call the generate_bids function with the required parameters
bid_data = generate_bids(
    advertisement_table=advertisement_data,
    customer_table=customer_data,
    n_data=1000,
    is_printed=False,
)

# Define headers for CSV files
manufactures_headers = ["manufacture_id", "manufacture_name"]
car_models_headers = ["model_id", "manufacture_id", "model_name"]
body_types_headers = ["body_type_id", "body_type_name"]
cars_header = [
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
location_headers = ["location_id", "city_name", "location"]
customer_headers = [
    "user_id",
    "first_name",
    "last_name",
    "email",
    "contact",
    "location_id",
]
advertisement_headers = [
    "ad_id",
    "user_id",
    "title",
    "price",
    "description",
    "car_id",
    "date_posted",
]
bid_headers = ["ad_id", "user_id", "bid_price", "bid_status", "datetime_bid"]


# Export data to CSV files in the "outputs" folder
list_to_csv(manufactures_data, "outputs", "manufactures.csv", manufactures_headers)
list_to_csv(car_models_data, "outputs", "car_models.csv", car_models_headers)
list_to_csv(body_type_data, "outputs", "body_types.csv", body_types_headers)
list_to_csv(cars_table_data, "outputs", "cars.csv", cars_header)
list_to_csv(location_data, "outputs", "locations.csv", location_headers)
list_to_csv(customer_data, "outputs", "user.csv", customer_headers)
list_to_csv(advertisement_data, "outputs", "ads.csv", advertisement_headers)
list_to_csv(bid_data, "outputs", "bid.csv", bid_headers)
