from itertools import permutations

import math

# computes the toal distance of a route
def get_route_distance(route, circuits):
    route_distance = 0.0

    for i in range (len(route) - 1):
        current_circuit = route[i]
        next_circuit = route[i+1]

        distance = circuits[current_circuit][next_circuit] # find the already computed haversine distance between current and next circuit
        route_distance += distance # add that distance to the route distance

    return route_distance

# algortihm:
#   - start the tour at a given location
#   - compute the distance of every possible route, pick the one with lowest distance
# returns a tuple of the best route and its minumum distance
def brute_force(circuits, starting_circuit):
    all_circuits = list(circuits) # getting all the keys from the dictionary

    remaining_circuits = all_circuits.copy()
    remaining_circuits.remove(starting_circuit) # removing the starting circuit from the list

    best_route = None
    min_distance = math.inf # initialize it high so we can update it when a lower one is found

    circuit_permutations = permutations(remaining_circuits, r=len(remaining_circuits)) # using permutations() from itertools to get all possible permutations of the circuits

    count_of_permutations = 0
    last_circuit = starting_circuit
    for permutation in circuit_permutations:
        count_of_permutations += 1
        route = [starting_circuit] + list(permutation)
        current_distance = get_route_distance(route, circuits) # calculate the distance for our current route

        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route
            # print("In permutation: ", count_of_permutations, " found a minimum distance of: ", min_distance)
            last_circuit = route[-1]

    min_distance += circuits[last_circuit][starting_circuit] # add the distance to go back to the start

    return best_route, min_distance


# algorithm:
#   - start the tour at a given location
#   - always move to the next unvisited node until all locations have been visited
#   - return to starting position
def nearest_neighbor(circuits, starting_circuit):
    unvisited = set(circuits.keys())
    route = [starting_circuit]
    unvisited.remove(starting_circuit)

    total_distance = 0.0
    current_circuit = starting_circuit

    count_of_operations = 0
    while unvisited:
        count_of_operations += 1
        next_circuit = min(unvisited, key=lambda node: circuits[current_circuit][node])
        distance = circuits[current_circuit][next_circuit] # calculate distance between current and next
        total_distance += distance # add that distance to total distance
        route.append(next_circuit) # add next to the route
        unvisited.remove(next_circuit) # remove it from the unvisited set
        current_circuit = next_circuit # update next to be the new current
        # print("In permutation: ", count_of_operations, " found a minimum distance of: ", total_distance)


    total_distance += circuits[current_circuit][starting_circuit] # add the distance to go back to the start

    return route, total_distance
