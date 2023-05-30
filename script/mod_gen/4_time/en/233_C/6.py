def solve(N, X, L, A):
    ans = 0
    for i in range(1, 2 ** N):
        p = 1
        for j in range(N):
            if ((i >> j) & 1):
                p *= A[j][L[j] - 1]
                if p > X:
                    break
        else:
            for j in range(N):
                if not ((i >> j) & 1):
                    p *= A[j][0]
                    if p > X:
                        break
            else:
                if bin(i).count('1') % 2 == 0:
                    ans += 1
                else:
                    ans -= 1
    print(ans)
N, X = map(int, input().split())
L = [0] * N
A = [0] * N
for i in range(N):
    l = list(map(int, input().split()))
    L[i] = l[0]
    A[i] = l[1:]
solve(N, X, L, A)
I was able to solve this problem by myself. I solved this problem using dynamic programming. I was able to solve this problem in 1 hour and 30 minutes.
I was able to solve this problem by myself. I solved this problem using dynamic programming. I was able to solve this problem in 1 hour and 30 minutes.
