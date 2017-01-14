#!/usr/bin/python

import sys #random, sys, locale, string
from optparse import OptionParser

class comm:
    def __init__(self, file1, file2):
        if (file1 == "-"):
            self.lines1 = sys.stdin.readLines()
        else:
            f1 = open(file1, 'r')
            self.lines1 = f1.readlines()
            f1.close()
        if (file2 == "-"):
            self.lines2 = sys.stdin.readLines()
        else:
            f2 = open(file2, 'r')
            self.lines2 = f2.readlines()
            f2.close()

def main():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE1 FILE2

Output a comparison of FILE1 and FILE2."""

    parser = OptionParser(version=version_msg,
                          usage=usage_msg)
    parser.add_option("-1",
                      action="store_true", dest="no1", default=False,
                      help="exclude column 1")
    parser.add_option("-2",
                      action="store_true", dest="no2", default=False,
                      help="exclude column 2")
    parser.add_option("-3",
                      action="store_true", dest="no3", default=False,
                      help="exclude column 3")
    parser.add_option("-u",
                      action="store_true", dest="unsorted", default=False,
                      help="passed in files are not sorted")

    options, args = parser.parse_args(sys.argv[1:])

    if len(args) != 2:  # needs file1, file2 as minimum
        if len(args) == 0:
            parser.error("no operands")
        if len(args) == 1:
            parser.error("missing operand after {0}".format(args[0]))
        if len(args) > 2:
            parser.error("too many operands")
    input_file1 = args[0]
    input_file2 = args[1]
    cols = []               # Array of arrays?

    try:
        comp = comm(input_file1, input_file2)
    except:
        parser.error("files cannot be compared: {0} and/or {1}".
                    format(input_file1, input_file2))

    # For unsorted -u files
    try:
        if (options.unsorted):
            for l1 in comp.lines1:
                added = False
                for l2 in comp.lines2:
                    if (l1 == l2):      # If in both, add to col3
                        cols.append([l1, 3])
                        comp.lines2.remove(l2)
                        added = True
                        break
                if (added == False):      # If not added to col3, add to col1
                    cols.append([l1, 1])
            for line2 in comp.lines2:
                cols.append([line2, 2])
    except:
        parser.error("failed to compare unsorted files")

    # For sorted files
    try:
        if (options.unsorted == False):
            i1 = 0
            i2 = 0
            while ((i1 < len(comp.lines1)) and (i2 < len(comp.lines2))):
                if (comp.lines1[i1] == comp.lines2[i2]):
                    cols.append([comp.lines1[i1], 3])
                    i1+=1
                    i2+=1
                elif (comp.lines1[i1] < comp.lines2[i2]):
                    cols.append([comp.lines1[i1], 1])
                    i1+=1
                else:
                    cols.append([comp.lines2[i2], 2])
                    i2+=1
            if (i1 != len(comp.lines1)):
                while (i1 < len(comp.lines1)):
                    cols.append([comp.lines1[i1], 1])
                    i1+=1
            elif (i2 < len(comp.lines2)):
                while (i2 < len(comp.lines2)):
                    cols.append([comp.lines2[i2], 2])
                    i2+=1
    except:
        parser.error("failed to compare sorted files")

    for i in cols:
        if (options.no1 == False and i[1] == 1):
            sys.stdout.write(i[0])
        elif (options.no2 == False and i[1] == 2):
            if (options.no1 == True):
                sys.stdout.write(i[0])
            else:
                sys.stdout.write("\t" + i[0])
        elif (options.no3 == False and i[1] == 3):
            if (options.no1 == True and options.no2 == True):
                sys.stdout.write(i[0])
            elif ((options.no1 == False and options.no2 == True) or (options.no1 == True and options.no2 == False)):
                sys.stdout.write("\t" + i[0])
            else:
                sys.stdout.write("\t\t" + i[0])

if __name__ == "__main__":
    main()
