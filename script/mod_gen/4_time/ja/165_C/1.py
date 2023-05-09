def dfs(A):
    if len(A) == N:
        score = 0
        for a, b, c, d in Q:
            if A[b-1] - A[a-1] == c:
                score += d
        return score
    else:
        last = A[-1]
        ans = 0
        for i in range(last, M+1):
            A.append(i)
            ans = max(ans, dfs(A))
            A.pop()
        return ans
N, M, Q = map(int, input().split())
Q = [list(map(int, input().split())) for _ in range(Q)]
ans = dfs([1])
print(ans)

if __name__ == '__main__':
    dfs()