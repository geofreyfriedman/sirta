import numpy as np
import random

chromosomes = int(input("chromosomes: "))
trials = int(input("trials: "))

data = np.zeros([trials, chromosomes], dtype=int)  # initializing array for data
for chromosome in range(chromosomes):
    print(f"Chromosome {chromosome + 1}: ")
    # user input:
    plus = int(input("plus: "))  # number of plus strand events in chromosome of interest
    minus = int(input("minus: "))  # number of minus strand events in chromosome of interest
    for trial in range(trials):
        # creates randomly ordered array of "+" and "-" with number of each corresponding to user's input
        dist = np.array(random.sample(["+", "-"], counts=[plus, minus], k=plus+minus))
        switches = 0
        for i in range(1, len(dist)):
            # calculates number of switches between plus and minus strand events
            if dist[i] != dist[i-1]:
                switches += 1
        data[trial, chromosome] = switches  # stores results for each trial into the "data" array

combined_sum = []
for n in range(trials):
    summation = [np.sum(data[n, :])]  # sums the n'th trial across all chromosomes
    combined_sum.append(summation)

# writing to text file:
pointer = open("switches.txt", "w")
pointer.write(str(combined_sum))
pointer.close()
