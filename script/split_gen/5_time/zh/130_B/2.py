def problem130_b():
    n, x = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0] * (n + 1)
    for i in range(1, n + 1):
        D[i] = D[i - 1] + L[i - 1]
        if D[i] > x:
            print(i)
            break
    else:
        print(n + 1)
