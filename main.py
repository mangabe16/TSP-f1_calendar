from itertools import islice
from circuits import load_circuit_data
from algorithms import brute_force_TSP, nearest_neighbor_TSP
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

    optimal_route, best_distance = brute_force_TSP(small_graph, first_circuit)
    print("The best route starting from ", first_circuit, " is ", optimal_route, " with a distance of: ", best_distance )

    optimal_route, best_distance = nearest_neighbor_TSP(small_graph, first_circuit)
    print("The best route starting from ", first_circuit, " is ", optimal_route, " with a distance of: ", best_distance )


    return 0





if __name__ == "__main__":
    main()
