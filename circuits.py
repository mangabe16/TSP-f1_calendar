import math
import pandas as pd

def haversine(coordinate1, coordinate2):
    """
    Computes straight-line distance (in kilometers) between two coordinates.
    """
    R = 6371.0  # Earth's mean radius in km

    latitude1, longitude1 = map(math.radians, coordinate1)
    latitude2, longitude2 = map(math.radians, coordinate2)

    delta_latitude = latitude2 - latitude1
    delta_longitude = longitude2 - longitude1

    # haversine of the central angle
    a = (math.sin(delta_latitude / 2) ** 2 +
         math.cos(latitude1) * math.cos(latitude2) * math.sin(delta_longitude / 2) ** 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)) # great-circle distance in radians

    # if we multuply the angle c by teh Earth's radius, we get the final distance in kilometers
    distance = R * c

    return round(distance,2)  # final distance rounded to 2 decimal places

def load_circuit_data():
    # loading the CSV file
    df = pd.read_csv("f1_data/circuits.csv")

    # filtering for only the circuits of interest (those in teh 2025 calendar)
    target_circuits_2025 = [
        "Albert Park Grand Prix Circuit",
        "Shanghai International Circuit",
        "Suzuka Circuit",
        "Bahrain International Circuit",
        "Jeddah Corniche Circuit",
        "Miami International Autodrome",
        "Autodromo Enzo e Dino Ferrari",
        "Circuit de Monaco",
        "Circuit de Barcelona-Catalunya",
        "Circuit Gilles Villeneuve",
        "Red Bull Ring",
        "Silverstone Circuit",
        "Circuit de Spa-Francorchamps",
        "Hungaroring",
        "Circuit Park Zandvoort",
        "Autodromo Nazionale di Monza",
        "Baku City Circuit",
        "Marina Bay Street Circuit",
        "Circuit of the Americas",
        "Autódromo Hermanos Rodríguez",
        "Autódromo José Carlos Pace",
        "Las Vegas Strip Street Circuit",
        "Losail International Circuit",
        "Yas Marina Circuit"
    ]

    f1_2025_df = df[df["name"].isin(target_circuits_2025)].copy()

    # dictionary of coordinates between a circuit and all the other circuits
    circuits_coordinates = {}

    # populating circuit_coordinates with coordinates in dataframe
    for name, lat, lng in zip(f1_2025_df['name'], f1_2025_df['lat'],f1_2025_df['lng']):
        latitute = float(lat)
        longitude = float(lng)
        circuits_coordinates[name] = (latitute, longitude)

    # dictionary of circuits, with the associated distances
    circuits = {}

    # populating the circuits dictionary with all circuits in the calendar, and the distance to
    # every other circuit (sourced from circuits_coordinates) in a corresponding sub dictionary
    for origin, origin_coordinates in circuits_coordinates.items(): # grab each circuit and coordinate pair in the dictionary
        circuits[origin] = {} # declare an empty dictionary for each individual circuit
        for destinations, destination_coordinates in circuits_coordinates.items(): # now iterate through all possible destinations of that circuit
            if destinations != origin: # disregard the circuit itself
                distance = haversine(origin_coordinates, destination_coordinates) # compute the distance between the origin circuit and the destination circuit
                circuits[origin][destinations] = distance # add the computed distance to that destination for that origin circuit

    return circuits
