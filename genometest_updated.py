import numpy as np
import random

chromosomes = int(input("chromosomes: "))
trials = int(input("trials: "))

data = np.zeros([chromosomes, trials, 16], dtype=int)  # reasonable to not expect run-lengths to exceed 16
for chromosome in range(chromosomes):
    print(f"Chromosome {chromosome + 1}: ")
    # user input:
    plus = int(input("plus: "))  # number of plus strand events in chromosome of interest
    minus = int(input("minus: "))  # number of minus strand events in chromosome of interest
    for trial in range(trials):
        # creates randomly ordered array of "+" and "-" with number of each corresponding to user's input
        dist = np.array(random.sample(["+", "-"], counts=[plus, minus], k=plus+minus))
        consecutive = 1
        numbers = []
        for i in range(1, len(dist)):  # calculates run-lengths in the "dist" array
            if dist[i] == dist[i-1]:
                consecutive += 1
            else:
                numbers.append(consecutive)
                consecutive = 1
        numbers.append(consecutive)  # appears again outside else block, appends last run-length (when i = len(dist))
        for i in range(1, 16):
            # counts the value of each run-length in the list (1-16, though once again, upper bound is arbitrary)
            # inserts that information into the array "data" for later analysis
            data[chromosome, trial, i - 1] = numbers.count(i)

combined_sum = []
for n in range(trials):
    summation = []
    for i in range(16):
        summation.append(np.sum(data[:, n, i]))  # sum of every chromosome's i'th run-length of the n'th trial
    combined_sum.append(summation)

# writing to text file:
pointer = open("genometest.txt", "w")
pointer.write(str(combined_sum))
pointer.close()
