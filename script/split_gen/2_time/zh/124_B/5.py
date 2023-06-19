def problems124_b():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        if h[i] >= max(h[:i]):
            count += 1
    print(count)
problems124_b()
