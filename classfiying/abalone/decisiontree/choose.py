import calentropy

def choose_best_feature_to_split(matrix):

    number_of_features = len(matrix[0]) - 1

    entropy = calentropy.calentropy(matrix)

    best_info_gain = 0.0

    best_feature = -1

    for i in range(number_of_features):


