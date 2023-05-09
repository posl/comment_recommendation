def main():
    N, M, Q = map(int, input().split())
    # print(N, M, Q)
    quad = []
    for i in range(Q):
        quad.append(list(map(int, input().split())))
    # print(quad)
    ans = 0
    for i in range(M):
        A = [i+1]
        ans = max(ans, dfs(N, M, Q, quad, A))
    print(ans)
