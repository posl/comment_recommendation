def main():
    from sys import stdin
    from collections import deque
    readline = stdin.readline
    N, L, R = map(int, readline().split())
    A = list(map(int, readline().split()))
    A = deque(A)
    ans = 0
    if L >= 0:
        ans = sum(A)
        ans += N * L
    elif R <= 0:
        ans = sum(A)
        ans += N * R
    else:
        for i in range(N):
            if A[i] >= 0:
                ans += A[i]
                A[i] = 0
            else:
                ans += R
                A[i] = R
        for i in range(N):
            if A[i] == 0:
                continue
            if L >= 0:
                ans += L
            else:
                ans += A[i]
                A[i] = 0
            for j in range(i+1, N):
                if A[j] == 0:
                    continue
                else:
                    ans += A[j]
                    A[j] = 0
                    break
    print(ans)

if __name__ == '__main__':
    main()