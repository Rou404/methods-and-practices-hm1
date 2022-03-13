import argparse

mylist = []

def bubble_sort(mylist):
    length = len(mylist)
    for i in range(length):
        for j in range(0, length-i-1):
            if mylist[j] > mylist[j+1]:
                aux = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = aux
    return mylist

def selection_sort(mylist):
    length = len(mylist)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if mylist[min_index] > mylist[j]:
                min_index = j
        aux = mylist[min_index]
        mylist[min_index] = mylist[i]
        mylist[i] = aux
    return mylist

def insertion_sort(mylist):
    length = len(mylist)
    for i in range(length):
        for j in range(i, length):
            if mylist[i] > mylist[j]:
                aux = mylist[i]
                mylist[i] = mylist[j]
                mylist[j] = aux
    return mylist

def merge_sort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        left = mylist[:mid]
        right = mylist[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                mylist[k] = left[i]
                i += 1
            else:
                mylist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            mylist[k] = left[i]
            i += 1
            k += 10.


        while j < len(right):
            mylist[k] = right[j]
            j += 1
            k += 1
    return mylist

def counting_sort(mylist):
    length = len(mylist)
    maxi = max(mylist)
    count = [0 for _ in range(maxi+1)]
    output = [0 for _ in range(length+1)]
    for i in mylist:
        count[i] += 1
    for j in range(1, maxi+1):
        count[j] += count[j-1]
    for i in mylist:
        output[count[i]] = i
        count[i] -= 1
    mylist = [x for x in output[1::]]
    return mylist

def radix_counter(mylist, digit):
    length = len(mylist)
    output = [0 for _ in length]
    count = []

function_map = {'bubble' : bubble_sort,
                'selection' : selection_sort,
                'insertion' : insertion_sort,
                'merge' : merge_sort,
                'counting' : counting_sort,
                'quick' : "quick",
                'radix'  : "radix.func"
                }


my_parser = argparse.ArgumentParser(description='Sorting algorithm')
my_parser.add_argument('-l','--list', help='List you want to be sorted example -l 1,26,12,54',type= str, required=True)
my_parser.add_argument('command', choices=function_map.keys())
args = my_parser.parse_args()
mylist = [int(x) for x in getattr(args, 'list').split(',')]
func = function_map[args.command]
print(func(mylist))