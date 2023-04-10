import numpy as np
import random


def sirta_distances(chromosome_length, number_of_sirtas):  # returns an array of the distances between sirtas
    indices = np.zeros([number_of_sirtas], dtype=int)
    distances = np.zeros([number_of_sirtas - 1])  # will hold the sirta distances for each chromosome

    for j in range(number_of_sirtas):
        indices[j] = random.randint(1, chromosome_length)  # chooses random indices to be sirta locations

    sorted_indices = np.sort(indices)  # sorts the 'indices' array in numerical order

    for n in range(1, number_of_sirtas):
        distance = sorted_indices[n] - sorted_indices[n-1]  # calculates numerical difference between adjacent sirtas
        distances[n - 1] = distance

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

big_array = np.zeros([trials, 16], dtype=int)  # this is the array that will store all the data, 16 bins of size 10,000
for trial in range(trials):
    for chromosome in range(chromosomes):
        # calls 'sirta_distances' function using values in the 'length_and_sirtas' array:
        a = sirta_distances(int(lengths_and_sirtas[0, chromosome]), int(lengths_and_sirtas[1, chromosome]))

        # bins the sirta_distances based on size:
        hist = np.histogram(a, bins=(0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000,
                                     120000, 130000, 140000, 150000, 160000))
        reformatted_hist = hist[0]  # np.histogram returns two arrays in a tuple, but only interested in the first one
        for i in range(16):
            big_array[trial, i] += int(reformatted_hist[i])  # adds the data to 'big_array'


# creates a txt file with the data
pointer = open(f"distance_between_sirtas_big.txt", "w")
pointer.write(str(big_array.tolist()))
pointer.close()



