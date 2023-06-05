def countNum(arr, l, r, x):
    count = 0
    for i in range(l-1, r):
        if arr[i] == x:
            count += 1
    return count
n = int(input())
arr = list(map(int, input().split()))
q = int(input())
for i in range(q):
    l, r, x = map(int, input().split())
    print(countNum(arr, l, r, x))
