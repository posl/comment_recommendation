def count_element(start, end, x):
    count = 0
    for i in range(start, end+1):
        if a[i] == x:
            count += 1
    return count
n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
    l, r, x = map(int, input().split())
    print(count_element(l-1, r-1, x))
