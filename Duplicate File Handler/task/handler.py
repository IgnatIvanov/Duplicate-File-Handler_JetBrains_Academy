import sys
import os


args = sys.argv  # we get the list of arguments

if len(args) > 1:
    # print(args[1])
    for root, dirs, files in os.walk('.\\' + args[1], topdown=True):
        for name in files:
            print(os.path.join(root, name))
        # for name in dirs:
        #     print(os.path.join(root, name))
else:
    print('Directory is not specified')
