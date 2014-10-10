import operator

def vote(classes):

    class_count = {}

    for classs in classes:

        if classs not in class_count.keys():

            class_count[classs] = 0

        class_count[classs] += 1

    sorted_class_count = sorted(class_count.iteritems(),
                                key = operator.itemgetter(1),
                                reverse = True
                               )

    return sorted_class_count[0][0]



