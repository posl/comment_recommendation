def swap(x):
    global arr
    global arr2
    global n
    global m
    global count
    global flag
    global flag2
    if flag == 0:
        arr2[x-1],arr2[x] = arr2[x],arr2[x-1]
        if arr2[x-1] == x-1:
            flag = 1
        if flag2 == 1:
            count += 1
        if count == m:
            flag2 = 0
            count = 0
    else:
        arr2[x-1],arr2[x] = arr2[x],arr2[x-1]
        if arr2[x] == x:
            flag = 0
        if flag2 == 1:
            count += 1
        if count == m:
            flag2 = 0
            count = 0
    return arr2
n,m = map(int,input().split())
arr = list(range(n))
arr2 = list(range(n))
count = 0
flag = 0
flag2 = 1
for i in range(m):
    x = int(input())
    arr2 = swap(x)
print(*arr2)

if __name__ == '__main__':
    swap()