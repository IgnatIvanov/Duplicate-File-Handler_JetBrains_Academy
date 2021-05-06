import sys
import os
import collections


args = sys.argv  # we get the list of arguments
file_format = '*'

if len(args) > 1:
    # print(args[1])
    print('Enter file format:')
    file_format = (str(input()))
    option = False

    while True:
        print(r'''
        Size sorting options:
1. Descending
2. Ascending

Enter a sorting option:''')
        n = int(input())
        if n == 1:
            option = True
            break
        elif n == 2:
            break
        else:
            print('Wrong option')

    search_results = dict()
    repeats = dict()

    for root, dirs, files in os.walk('.\\' + args[1] + '*.' + file_format, topdown=True):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            search_results[path] = size
            repeats.setdefault(size, 0)
            repeats[size] += 1
            # search_results.update(path=size)
        # for name in dirs:
        #     print(os.path.join(root, name))

    for size, n in collections.OrderedDict(sorted(repeats.items(), reverse=option)):
        if n > 1:
            print('{} bytes'.format(n))
            for key, value in search_results:
                if value == n:
                    print(key)
            print()

    # {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    # search_results = {(sorted(search_results.items(), key=lambda item: item[1], reverse=option))}
    # Getting uniq file size values
    # files_sizes_set = set()
    # files_sizes_list = list()
    # for value in search_results.values():
    #     files_sizes_set.add(value)
    # for value in files_sizes_set:
    #     files_sizes_list.append(value)
    # files_sizes_list.sort(reverse=option)



    # Countiong sizes repeats
    # dict(sorted(x.items(), key=lambda item: item[1]))
else:
    print('Directory is not specified')
