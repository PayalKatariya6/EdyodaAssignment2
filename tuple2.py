a =[(5, 7), (12, 4), (20, 13), (45, 2)]
print("List of Tuple before sorting : " + str(a))


listLen = len(a); 
for i in range(0, listLen):
    for j in range(0, listLen - i - 1):
        if(a[j][-1] > a[j + 1][-1]):
            b = a[j]
            a[j] = a[j + 1]
            a[j + 1] = b

print("List of Tuple after sorting : " + str(a))