import sys
import re
from lib.common import *

# Create path variable for file
NAME = "EDITNAME"
PATH = sys.path[0]+f"\\challenges\\{NAME}"


'''
Follow these steps to add a template
 1. Create a folder for the challenge number (i.e. 'one', 'two', 'three', etc.)
 2. Copy the contents of this template folder into the new numbered folder
 3. Add the folder name to the __all__ variable in `challenges/__init__.py`
 4. Import the new task inside `main.py`
 5. change EDITNAME in NAME, task_EDITNAME
 --- Once all are completed you can delete this comment ---
'''

class task_EDITNAME():
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
        # Put your code here
        pass