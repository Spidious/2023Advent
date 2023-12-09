import sys
import re
from lib.common import *

# Create path variable for file
NAME = "one"
PATH = sys.path[0]+f"\\challenges\\{NAME}"


class task_one():
    def __init__(self):
        try:
            # get the file input
            self.infile = getFile(f'{PATH}\\in.txt')
        except:
            # Create the file and raise error
            with open(f'{PATH}\\in.txt', 'r') as fp:
                fp.write('Replace the contents of this file with the provided input')
            raise Exception(f"Provide the input using the challenges/{NAME}/in.txt file")

    def challenge(self):
        '''
        given an input 
        sample:
            1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet

        Find the first and last numerical input in each row and output a list 

        example: 
            12
            38
            15
            77

        Adding these together will produce the sum 142

        RESULT: find the sum of in.txt
        '''
        # For fun, I did the entire challenge in one line
        rowSum = sum([int(f"{row[0]}{row[-1]}") for row in [re.sub("[^0-9]", "", f"{row}") for row in self.infile]])

        # Output the sum
        print(rowSum)


