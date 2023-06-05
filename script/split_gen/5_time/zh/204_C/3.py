def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            cnt = 0
            for k in range(M):
                if A[k] == i+1 and B[k] == j+1:
                    cnt += 1
                if A[k] == j+1 and B[k] == i+1:
                    cnt += 1
            ans += cnt * (cnt-1) // 2
    print(ans)
