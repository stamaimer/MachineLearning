from numpy import *

def normalize(matrix):

    mins = matrix.min(0)                               #cal the min value for each column
    maxs = matrix.max(0)                               #cal the max value for each column

    ranges = maxs - mins                                #cal the range for each column

    normalized_matrix = zeros(shape(matrix))

    number_of_rows = matrix.shape[0]

    normalized_matrix = matrix - tile(mins, (number_of_rows, 1))
    normalized_matrix = normalized_matrix / tile(ranges, (number_of_rows, 1))

    return normalized_matrix
