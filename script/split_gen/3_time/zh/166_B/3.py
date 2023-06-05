def solve():
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    #print(N, K, d, A)
    cnt = 0
    for i in range(N):
        flag = False
        for j in range(K):
            if i+1 in A[j]:
                flag = True
        if not flag:
            cnt += 1
    print(cnt)
