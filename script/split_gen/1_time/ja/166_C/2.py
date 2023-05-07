def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a-1)
        B.append(b-1)
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if A[j] == i:
                if H[i] <= H[B[j]]:
                    flag = False
                    break
            elif B[j] == i:
                if H[i] <= H[A[j]]:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)
