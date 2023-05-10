def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = [p[i] - 1 for i in range(n)]
    visited = [False] * n
    max_score = -10 ** 18
    for i in range(n):
        if visited[i]:
            continue
        score = 0
        visited[i] = True
        current = i
        cycle = []
        while True:
            current = p[current]
            score += c[current]
            visited[current] = True
            cycle.append(current)
            if current == i:
                break
        cycle_len = len(cycle)
        cycle_score = 0
        for j in range(cycle_len):
            cycle_score += c[cycle[j]]
            max_score = max(max_score, cycle_score)
        if score > 0:
            cycle_score = 0
            for j in range(cycle_len):
                cycle_score += c[cycle[j]]
                if j + 1 > k:
                    break
                max_score = max(max_score, cycle_score + (k - j - 1) // cycle_len * score)
    print(max_score)
