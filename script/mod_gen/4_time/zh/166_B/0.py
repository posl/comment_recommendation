def solve():
    N, K = map(int, input().split())
    d = [0] * K
    A = []
    for i in range(K):
        d[i] = int(input())
        A.append(list(map(int, input().split())))
    cnt = 0
    for i in range(N):
        for j in range(K):
            if i+1 in A[j]:
                break
        else:
            cnt += 1
    print(cnt)
solve()
