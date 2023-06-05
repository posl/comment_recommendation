def problems170_d():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [True] * n
    for i in range(n):
        if b[i]:
            for j in range(i + 1, n):
                if a[j] % a[i] == 0:
                    b[j] = False
    print(sum(b))
