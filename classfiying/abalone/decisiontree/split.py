def split(matrix, axis, value):

    ret_marix = []

    for features in matrix:

        if features[axis] == value:

            ret_features = features[:axis]

            ret_features.extend(features[axis+1:])

            ret_marix.append(ret_features)

    return ret_marix
