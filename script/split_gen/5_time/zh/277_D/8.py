def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(M)
    B = []
    cnt = 1
    for i in range(N):
        if A[i] != A[i+1]:
            B.append(cnt)
            cnt = 1
        else:
            cnt += 1
    ans = 0
    B.sort()
    for i in range(len(B)):
        if B[i] % 2 == 0:
            ans += B[i]-1
        else:
            ans += B[i]
    print(ans)
