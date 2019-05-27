# -*- coding:utf-8 -*-
import itertools

def merge_sort(array):
    mid = len(array)
    if mid > 1:
        left = merge_sort(array[:(mid/2)])
        right = merge_sort(array[(mid/2):])
        array = []
        while len(left) != 0 and len(right) != 0:
            if left[0] < right[0]:
                array.append(left.pop(0))
            else:
                array.append(right.pop(0))
        if len(left) != 0:
            array.extend(left)
        elif len(right) != 0:
            array.extend(right)
    return array


string = raw_input()
list1 = string.split()
list1 = merge_sort(list1)
n = 15

all_dict = {} #key:sorted  value:non-sorted
dict_list = [] #sorted
f = open('dictionary.txt','r')
for row in f:
    str1 = row.strip().lower()
    l = merge_sort(list(str1))
    str2 = ''.join(l)
    all_dict[str2] = str1
    dict_list.append(str2)
merge_sort(dict_list) #sorted

all_list = [] #候補
all_list.append(''.join(str(a) for a in list1))

while n > 1:
    list2 = list(itertools.combinations(list1, n)) #組み合わせ
    list3 = []
    for a in list2:
        list3.append(''.join(str(b) for b in a))
    all_list = all_list + list3
    n -= 1

for a in all_list:
    if (a in all_dict) == True:
        print all_dict[a]

