def problems124_b():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        flag = True
        for j in range(i):
            if H[i] < H[j]:
                flag = False
        if flag:
            count += 1
    print(count)
