def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [p-1 for p in P]
    visited = [False] * N
    visited[0] = True
    score = [0] * N
    score[0] = C[0]
    cycle = []
    cycle_score = []
    cycle_score.append(score[0])
    cycle.append(0)
    while True:
        p = P[cycle[-1]]
        if visited[p]:
            break
        visited[p] = True
        cycle.append(p)
        score[p] = score[cycle[-2]] + C[p]
        cycle_score.append(score[p])
    cycle_length = len(cycle)
    if K <= cycle_length:
        return max(cycle_score[:K])
    else:
        cycle_sum = sum(cycle_score)
        cycle_max = max(cycle_score)
        cycle_sum += max(0, cycle_sum) * ((K - cycle_length) // cycle_length)
        cycle_max = max(cycle_max, cycle_max + max(0, cycle_sum) * ((K - cycle_length) % cycle_length))
        return cycle_max
print(solve())
