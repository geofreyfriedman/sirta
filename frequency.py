import numpy as np
import random

trials = int(input("Number of trials: "))

occurrences = []
for trial in range(trials):
    big_array = np.arange(1, 21923)  # [1, 2, 3, 4, ... 21921, 21922]
    for i in range(30):
        big_array[random.randint(0, len(big_array)-1)] = 0  # sets 30 random index values in big_array equal to 0
    num_sites = np.count_nonzero(big_array[0:300] == 0)  # counts elements in initial 300 indices of big_array that = 0
    occurrences.append(num_sites)

# writing to a text file:
pointer = open("sirta_probability.txt", "w")
pointer.write(str(occurrences))
pointer.close()
