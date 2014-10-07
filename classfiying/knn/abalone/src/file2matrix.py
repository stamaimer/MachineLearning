from numpy import *

def file2matrix(filename):

    file = open(filename)

    line = file.readline()

    number_of_feats = len(line.split(',')) - 1
    
    number_of_lines = len(file.readlines()) + 1

    martrix = zeros((number_of_lines, number_of_feats))                                     #create a numpy martrix to return

    labels = []                                                                             #the last column in the file

    file = open(filename)

    index = 0

    for line in file.readlines():

        features = line.split(',')

        martrix[index, :] = array(features[0:number_of_feats])

        labels.append(int(features[-1]))

        index = index + 1

    return martrix, labels
