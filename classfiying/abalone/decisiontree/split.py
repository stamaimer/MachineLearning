def split(matrix, axis, value):

    ret_matrix = []

    for features in matrix:

        if features[axis] == value:

            ret_features = features[:axis].tolist()

            ret_features.extend(features[axis+1:])

            ret_matrix.append(ret_features)

    return ret_matrix
