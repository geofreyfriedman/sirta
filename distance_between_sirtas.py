import numpy as np
import random


def sirta_distances(chromosome_length, number_of_sirtas):  # returns a list of the distances between sirtas
    indices = np.zeros([number_of_sirtas], dtype=int)  # initializes an array
    distances = []  # will hold the sirta distances for each chromosome

    for i in range(number_of_sirtas):
        indices[i] = random.randint(1, chromosome_length)  # chooses random indices to be sirta locations

    sorted_indices = np.sort(indices)  # sorts the 'indices' array in numerical order

    for n in range(1, number_of_sirtas):
        distance = sorted_indices[n] - sorted_indices[n-1]  # calculates numerical difference between adjacent sirtas
        distances.append(distance)

    return distances


# ui:
trials = int(input("trials: "))
chromosomes = int(input("chromosomes: "))

# everything below here is largely to optimize the process for running multiple trials at once:

lengths_and_sirtas = np.zeros([2, chromosomes])  # initializes array to hold the user's input across multiple trials

for chromosome in range(chromosomes):
    print()
    print(f"chromosome {chromosome + 1}: ")
    # stores the users inputted lengths and sirtas for each chromosome in the 'length_and_sirtas' array:
    lengths_and_sirtas[0, chromosome] = int(input("length: "))
    lengths_and_sirtas[1, chromosome] = int(input("sirtas: "))

for trial in range(trials):
    big_list = []

    # calls 'sirta_distances' function using values in the 'length_and_sirtas' array
    for chromosome in range(chromosomes):
        big_list.append(sirta_distances(int(lengths_and_sirtas[0, chromosome]), int(lengths_and_sirtas[1, chromosome])))

    # creates different txt files for each trial (with the data)
    pointer = open(f"distance_between_sirtas{trial + 1}.txt", "w")
    pointer.write(str(big_list))
    pointer.close()



