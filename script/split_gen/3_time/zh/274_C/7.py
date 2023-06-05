def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*(2*n+1)
    for i in range(n):
        b[a[i]] = i+1
    for i in range(1, 2*n+1):
        j = i
        while j != 1:
            print(b[j], end=' ')
            j //= 2
        print(0)
