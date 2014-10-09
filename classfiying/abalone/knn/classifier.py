from numpy import *
import operator

def none2int(var):

    if var == None:

        return 0
    else:

        return var

def classify(instance, matrix, labels, k):

    number_of_rows = matrix.shape[0]

    diff_matrix = tile(instance, (number_of_rows, 1)) - matrix

    sqrt_matrix = diff_matrix ** 2

    sqrt_distan = sqrt_matrix.sum(axis = 1)

    distances = sqrt_distan ** 0.5

    sorted_distances = distances.argsort()

    class_count = {}

    for i in range(k):

        tmp = labels[sorted_distances[i]]

        class_count[tmp] = none2int(class_count.get(tmp)) + 1

    sorted_class_count = sorted(class_count.iteritems(),
                                key = operator.itemgetter(1),
                                reverse = True)

    return sorted_class_count[0][0]
