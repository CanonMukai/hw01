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

def calc(str1):
    sum1 = 0
    for i in range(len(str1)):
        if (str1[i] in point2) == True:
            sum1 += 2
        elif (str1[i] in point3) == True:
            sum1 += 3
        else:
            sum1 += 1
    sum1 += 1
    return sum1*sum1

point2 = {'c':2,'f':2,'h':2,'l':2,'m':2,'p':2,'v':2,'w':2,'y':2}
point3 = {'j':3,'k':3,'qu':3,'x':3,'z':3}


all_dict = {} #key:sorted  value:non-sorted
dict_list = [] #sorted
f = open('dictionary.txt','r')
for row in f: #辞書をソート・all_dictに保存
    str1 = row.strip().lower()
    l = merge_sort(list(str1))
    str2 = ''.join(l)
    all_dict[str2] = str1
    dict_list.append(str2)
merge_sort(dict_list) #sorted
print '準備OK'


while True:
    
    string = raw_input()
    list1 = string.split()
    list1 = merge_sort(list1)
    n = 15

    all_list = [] #候補
    all_list.append(''.join(str(a) for a in list1))
    print all_list
    
    while n > 1:
        list2 = list(itertools.combinations(list1, n)) #組み合わせ
        list3 = []
        for a in list2:
            list3.append(''.join(str(b) for b in a))
        all_list = all_list + list3
        n -= 1
            
    point_dict = {}
    point_list = []
    for a in all_list:
        if (a in all_dict) == True:
            #print all_dict[a]
            num = calc(a)
            point_dict[num] = a
            point_list.append(num)
        
    point_list = merge_sort(point_list)
    print point_dict
    print all_dict[point_dict[point_list[len(point_list)-1]]]
    print '====='
    
