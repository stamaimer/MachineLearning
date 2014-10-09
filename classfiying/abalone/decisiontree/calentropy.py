from math import log

def calentropy(matrix):

    number_of_rows = len(matrix)

    label_counts = {}

    for features in matrix:

        current_label = features[-1]

        if current_label not in label_counts.keys():

            label_counts[current_label] = 0

        label_counts[current_label] += 1

    entropy = 0.0

    for key in label_counts:

        probability = float(label_counts[key]) / number_of_rows

        entropy -= probability * log(probability, 2)

    return entropy
