import re
import sys

ifile = open(sys.argv[1], 'r')
ofile = open(sys.argv[2], 'w')

for line in ifile.readlines():

    line = re.sub('M', '1', line)       #map male to 1
    line = re.sub('F', '0', line)       #map female to 0
    line = re.sub('I', '2', line)       #map infant to 2

    ofile.write(line)

ifile.close()
ofile.close()


