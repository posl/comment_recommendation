def problems152_c():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 1
    min = p[0]
    for i in range(1, n):
        if p[i] < min:
            cnt += 1
            min = p[i]
    print(cnt)
