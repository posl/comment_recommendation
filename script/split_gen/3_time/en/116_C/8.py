def solve():
    n = int(input())
    h = [int(x) for x in input().split()]
    # print(n, h)
    count = 0
    for i in range(1, n):
        if h[i] < h[i-1]:
            count += h[i-1] - h[i]
    print(count)
