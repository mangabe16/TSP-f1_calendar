from itertools import islice
from circuits import load_circuit_data
from algorithms import brute_force, nearest_neighbor
from genetic_algorithm import genetic_algorithm
import math


def main():

    # getting the circuits dictionary from circuits.py module
    circuits = load_circuit_data()


    # print(circuits["Baku City Circuit"]["Yas Marina Circuit"])
    # print(circuits["Baku City Circuit"])

    # using the opening circuit as the starting point, but the choice of the starting node actually doesn'y
    # affect the solution!
    first_circuit = "Albert Park Grand Prix Circuit"

    # full graph is taking too long, so I'm going to use a small graph for now
    small_graph = dict(islice(circuits.items(), 8))

    optimal_route_brute_force, distance_brute_force = brute_force(small_graph, first_circuit)
    print(f"Brute Force Algorithm: {distance_brute_force} km")
    print("Best Route:", optimal_route_brute_force, "\n")

    optimal_route_NN, distance_NN = nearest_neighbor(small_graph, first_circuit)
    print(f"Nearest neighbor Algorithm: {distance_NN} km")
    print("Best Route:", optimal_route_NN, "\n")

    ga_route, ga_dist = genetic_algorithm(small_graph, first_circuit)
    print(f"Genetic Algorithm: {ga_dist} km")
    print("Best GA Route:", ga_route, "\n")

    return 0





if __name__ == "__main__":
    main()
