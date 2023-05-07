def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A.sort()
    if N == 1:
        print(A[0])
        return
    if A[0] == 0:
        print(0)
        return
    cnt = 0
    for i in range(N - 1):
        if A[i] != A[i + 1] - 1:
            cnt += 1
    if cnt <= 1:
        print(0)
        return
    ans = 0
    for a in A:
        ans += M - a
    print(ans)
