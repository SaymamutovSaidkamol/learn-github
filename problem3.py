def lists(ls, n):
    ls1 = []
    for i in range(n):
        ls1.append(ls[i])
        ls1.append(ls[i+n])
    return ls1

# 1 chi examole
list1= [1,2,3,4,4,3,2,1]

n1 = int(len(list1)/2)
result = lists(list1, n1)
print(result)

# 2 chi example
list2 = [2,5,1,3,4,7]

n2 = int(len(list2)/2)
result = lists(list2, n2)
print(result)

# 3 chi example
list3 = [1,1,2,2]

n3 = int(len(list3)/2)
result = lists(list3, n3)
print(result)