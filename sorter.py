import argparse
from timeit import default_timer as timer

mylist = []


def bubble_sort(mylist):
    start = timer()
    length = len(mylist)
    for i in range(length):
        for j in range(0, length - i - 1):
            if mylist[j] > mylist[j + 1]:
                aux = mylist[j]
                mylist[j] = mylist[j + 1]
                mylist[j + 1] = aux
    end = timer()
    return end - start


def selection_sort(mylist):
    start = timer()
    length = len(mylist)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if mylist[min_index] > mylist[j]:
                min_index = j
        aux = mylist[min_index]
        mylist[min_index] = mylist[i]
        mylist[i] = aux
    end = timer()
    return end - start


def insertion_sort(mylist):
    start = timer()
    length = len(mylist)
    for i in range(length):
        for j in range(i, length):
            if mylist[i] > mylist[j]:
                aux = mylist[i]
                mylist[i] = mylist[j]
                mylist[j] = aux
    end = timer()
    return end - start


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
            k += 10.0

        while j < len(right):
            mylist[k] = right[j]
            j += 1
            k += 1

def merge_sort_timer(mylist):
    start = timer()
    merge_sort(mylist)
    end = timer()
    return end - start

def counting_sort(mylist):
    start = timer()
    length = len(mylist)
    maxi = max(mylist)
    count = [0 for _ in range(maxi + 1)]
    output = [0 for _ in range(length + 1)]
    for i in mylist:
        count[i] += 1
    for j in range(1, maxi + 1):
        count[j] += count[j - 1]
    for i in mylist:
        output[count[i]] = i
        count[i] -= 1
    mylist = [x for x in output[1::]]
    end = timer()
    return end - start


def heapify(mylist, length, index):
    maxi = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < length and mylist[maxi] < mylist[left]:
        maxi = left
    if right < length and mylist[maxi] < mylist[right]:
        maxi = right
    if maxi != index:
        mylist[index], mylist[maxi] = mylist[maxi], mylist[index]

        heapify(mylist, length, maxi)


def heap_sort(mylist):
    start = timer()
    length = len(mylist)

    for index in range(length // 2 - 1, -1, -1):
        heapify(mylist, length, index)

    for index in range(length - 1, 0, -1):
        mylist[index], mylist[0] = mylist[0], mylist[index]
        heapify(mylist, index, 0)
    end = timer()
    return end - start


def radix_counter(mylist, digit):
    length = len(mylist)
    output = [0 for _ in range(length)]
    count = [0 for _ in range(10)]
    for i in range(0, length):
        index = mylist[i] // digit
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = length - 1
    while i >= 0:
        index = mylist[i] // digit
        output[count[index % 10] - 1] = mylist[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(mylist)):
        mylist[i] = output[i]

def radix_sort(mylist):
    start = timer()
    maxi = max(mylist)
    exp = 1
    while maxi / exp > 1:
        radix_counter(mylist, exp)
        exp *= 10
    end = timer()
    return end - start


def partition(mylist, low, high):
    pivot = mylist[high]
    i = low - 1
    for j in range(low, high):
        if mylist[j] <= pivot:
            i += 1
            mylist[i], mylist[j] = mylist[j], mylist[i]
    mylist[i + 1], mylist[high] = mylist[high], mylist[i + 1]
    return i + 1


def quick_sort(mylist, low, high):
    start = timer()
    if low < high:
        pi = partition(mylist, low, high)
        quick_sort(mylist, low, pi - 1)
        quick_sort(mylist, pi + 1, high)
    end = timer()
    return end - start


function_map = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "heap": heap_sort,
    "counting": counting_sort,
    "quick": quick_sort,
    "radix": radix_sort,
    "all": "all",
}


my_parser = argparse.ArgumentParser(description="Sorting algorithm")
my_parser.add_argument(
    "-l", "--list", help="List you want to be sorted example -l 1,26,12,54", type=str
)
my_parser.add_argument("command", choices=function_map.keys())
args = my_parser.parse_args()
func = function_map[args.command]
if getattr(args, "list"):
    print('here')
    mylist = [int(x) for x in getattr(args, "list").split(",")]
    if func == quick_sort:
        print(func(mylist, 0, len(mylist) - 1))
    else:
        print(func(mylist))
elif getattr(args, "command") == "all":
    j = open("Lists")
    mylist = [int(x) for x in j.readline().split(" ")]
    copy = [x for x in mylist]
    print(bubble_sort(mylist))
    mylist = [x for x in copy]
    print(insertion_sort(mylist))
    mylist = [x for x in copy]
    print(selection_sort(mylist))
    mylist = [x for x in copy]
    print(radix_sort(mylist))
    mylist = [x for x in copy]
    print(counting_sort(mylist))
    mylist = [x for x in copy]
    print(merge_sort_timer(mylist))
    mylist = [x for x in copy]
    print(quick_sort(mylist, 0, len(mylist) - 1))
    mylist = [x for x in copy]
    print(heap_sort(mylist))
    mylist = [x for x in copy]
