def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = [None] * n
    for i in range(n):
        b[a[i]-1] = i+1
    print(" ".join(map(str, b)))
