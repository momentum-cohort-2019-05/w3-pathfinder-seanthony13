from PIL import image
from ElevationMap_class import ElevationMap

def read_lines_of_ints(text):
    """Given a string with integers in it, return a list of those integers.
    """
    ints = []
    ints_as_strs = split_line(text)
    # below is equivalent code to the following for loop
    # index = 0
    # while index < len(ints_as_strs):
    #   int_as_str = ints_as_strs[index]
    #   index += 1
    for ints_as_str in ints_as_strs:
        ints.append(int(int_as_str))
    return ints

def split_line(line):
    return line.split()

def read_file_into_list(filename):
    """Given a file, return a list of each line in the file as a string.
    """
    with open(filename) as file:
        return file.readlines()

def read_file_into_ints(filename):
    """Given a filename, read that file and then convert it to a list of lists of ints.
    Example:
    We have a file with these contents:
    1 2
    3 4
    The return value would be [[1,2], [3,4]]
    """
    lines = read_file_into_list(filename)
    list_of_lists = []
    for line in lines:
        list_of_lists.append(read_lines_of_ints))
    return list_of_lists



# print(read_file_into_ints('elevation_test.txt'))

