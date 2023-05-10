def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [p - 1 for p in P]
    max_score = -10 ** 18
    for i in range(N):
        visited = [False] * N
        visited[i] = True
        score = C[i]
        j = P[i]
        while not visited[j]:
            visited[j] = True
            score += C[j]
            j = P[j]
        if score > max_score:
            max_score = score
        if K > 1:
            cycle_score = score
            cycle_length = 1
            j = P[i]
            while j != i:
                cycle_score += C[j]
                j = P[j]
                cycle_length += 1
            cycle_score += (K - 2) // cycle_length * max(0, cycle_score)
            if cycle_score > max_score:
                max_score = cycle_score
    return max_score
print(solve())
