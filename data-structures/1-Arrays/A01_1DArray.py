arr_1 = [10, 3, 7, 15]
arr_2 = [10.0, 3, "second", 5]

# printing all items
print(arr_1[:])
print(arr_2[:])

# random indexing
print(arr_1[1])
print(arr_2[2])

# linear search O(n)-time complexity
max = arr_1[0]
for ele in arr_1:
    if ele > max:
        print(ele)

