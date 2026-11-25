from itertools import permutations
from itertools import islice
from circuits import load_circuit_data
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
    small_graph = dict(islice(circuits.items(), 5))

    optimal_route, best_distance = brute_force_TSP(small_graph, first_circuit)
    print("The best route starting from ", first_circuit, " is ", optimal_route, " with a distance of: ", best_distance )
    return 0


def get_route_distance(route, circuits):
    route_distance = 0.0

    for i in range (len(route) - 1):
        current_circuit = route[i]
        next_circuit = route[i+1]

        distance = circuits[current_circuit][next_circuit] # find the distance between current and next circuit in the dictionary
        route_distance += distance # add that distance to the route distance

    return route_distance

# returns a tuple of the best route and its minumum distance
def brute_force_TSP(circuits, starting_circuit):
    all_circuits = list(circuits) # getting all the keys from the dictionary

    remaining_circuits = all_circuits.copy()
    remaining_circuits.remove(starting_circuit) # removing the starting circuit from the list

    best_route = None
    min_distance = math.inf # initialize it high so we can update it when a lower one is found

    circuit_permutations = permutations(remaining_circuits, r=len(remaining_circuits)) # using permutations() from itertools to get all possible permutations of the circuits

    count_of_permutations = 0
    for permutation in circuit_permutations:
        count_of_permutations += 1
        route = [starting_circuit] + list(permutation)
        current_distance = get_route_distance(route, circuits) # calculate the distance for our current route

        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route
            print("In permutation: ", count_of_permutations, " found a minimum distance of: ", min_distance)

    return best_route, min_distance

if __name__ == "__main__":
    main()
