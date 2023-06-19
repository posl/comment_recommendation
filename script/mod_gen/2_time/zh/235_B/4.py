def solution():
    n = int(input())
    h = list(map(int, input().split()))
    last = h[0]
    for i in range(1, n):
        if h[i] > last:
            last = h[i]
    print(last)
solution()
