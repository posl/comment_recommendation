def main():
    # Read input
    N, M, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(Q)]
    # Initialize
    ans = 0
    A = sorted(A, key=lambda x: x[3], reverse=True)
    for a in A:
        if a[0] == 1:
            a.append([1, M])
        elif a[1] == N:
            a.append([1, M])
        else:
            a.append([a[0]-1, a[1]+1])
    # Recursive function
    def rec(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, ans):
        if len(A) == 0:
            ans = max(ans, sum(B))
            return ans
        else:
            a = A.pop()
            for i in range(a[2]):
                for j in range(a[2]-i):
                    if i+j == a[2]:
                        if a[0] <= a[3][0] <= a[1]:
                            B[a[3][0]-1] += 1
                        if a[0] <= a[3][1] <= a[1]:
                            B[a[3][1]-1] += 1
                        ans = rec(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, ans)
                        if a[0] <= a[3][0] <= a[1]:
                            B[a[3][0]-1] -= 1
                        if a[0] <= a[3][1] <= a[1]:
