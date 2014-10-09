import calentropy
import split

def choose_best_feature_to_split(matrix):

    number_of_features = len(matrix[0]) - 1

    base_entropy = calentropy.calentropy(matrix)

    best_info_gain = 0.0

    best_feature = -1

    for i in range(number_of_features):
	
	features = [row[i] for row in matrix]

	unique_features = set(features)

	inst_entropy = 0.0

	for feature in unique_features:

		splited_matrix = split.split(matrix, i, feature)

		probability = len(splited_matrix) / float(len(matrix))

		inst_entropy += probability * calentropy.calentropy(splited_matrix)

	info_gain = base_entropy - inst_entropy

	if(info_gain > best_info_gain):

		best_info_gain = info_gain

		best_feature = i

    return best_feature	 
