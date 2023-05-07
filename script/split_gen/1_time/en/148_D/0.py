def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        if A[0] == 1:
            print(0)
        else:
            print(-1)
        return
    if A[0] != 1:
        print(-1)
        return
    ans = 0
    for i in range(1, N):
        if A[i] == 1:
            ans += 1
            continue
        if A[i] - A[i - 1] == 1:
            ans += 1
            continue
        if A[i] - A[i - 1] > 1:
            print(-1)
            return
    print(N - ans)
