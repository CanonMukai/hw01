
def make_dict(str1):
    dict1 = {}
    for i in range(len(str1)):
        str2 = str1.lower()
        if (str2[i] in dict1) == True:
            j = int(dict1[str2[i]])
            j += 1
            dict1[str2[i]] = j
        else:
            dict1[str2[i]] = 1
    return dict1

a = ' '
while a != 'q':
    f = open('dictionary.txt', 'r')
    print 'Please input letters like "xolsae"'
    a = raw_input()
    if a == 'q':
        break
    dict = make_dict(a)
    print 'You can use these words,'
    for row in f:
        str = row.strip()
        dict1 = make_dict(str)
        if dict == dict1:
            print str
    
f.close()
