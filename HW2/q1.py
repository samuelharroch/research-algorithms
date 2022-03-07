'''
https://stackoverflow.com/questions/2349991/how-to-import-other-python-files
'''

import sys

module_file_name = sys.argv[1]
module_name = module_file_name[:-3]
module = __import__(module_name)

with open(sys.argv[2] , 'w') as html:
    sys.stdout = html
    help(module)
    sys.stdout = sys.__stdout__
