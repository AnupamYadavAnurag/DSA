arr = [1, 2, 1, 3, 2, 1]
hashmap = {}


for num in arr:
    hashmap[num] = hashmap.get(num, 0) + 1


q = int(input("Enter number of queries: "))
for _ in range(q):
    x = int(input("Enter element: "))
print(hashmap.get(x, 0))