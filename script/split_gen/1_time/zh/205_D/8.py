def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    a.sort()
    a.append(float('inf'))
    j = 0
    for i in range(q):
        while k[i] > a[j]:
            k[i] += 1
            j += 1
        print(k[i])
