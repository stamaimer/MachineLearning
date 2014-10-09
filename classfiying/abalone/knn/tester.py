import file2matrix
import classifier
import normalize

def tester():

    matrix, labels = file2matrix.file2matrix('../data/abalone')

    normalized_matrix, ranges, mins = normalize.normalize(matrix)

    number_of_rows = normalized_matrix.shape[0]

    number_of_test = int(number_of_rows * 0.1)

    error_count = 0.0

    for i in range(number_of_test):

        result = classifier.classify(normalized_matrix[i, :],
                                     normalized_matrix[number_of_test:number_of_rows, :],
                                     labels[number_of_test:number_of_rows], 20)

        print "the classifier's prediction is %d, the real answer is %d" % (result, labels[i])

        if(result != labels[i]):

            error_count = error_count + 1.0

    print "the error rate is %f" %  (error_count / float(number_of_test))
