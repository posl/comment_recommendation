def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    score = 0
    for i in range(N):
        if P[i] != 0:
            j = i
            cycle = []
            while True:
                cycle.append(C[j])
                P[j], j = 0, P[j] - 1
                if j == i:
                    break
            cycle_sum = sum(cycle)
            cycle_len = len(cycle)
            max_cycle = 0
            for j in range(cycle_len):
                max_cycle = max(max_cycle, cycle[j])
                if j + 1 <= K:
                    max_cycle = max(max_cycle, cycle[j] + cycle_sum * ((K - j - 1) // cycle_len))
            score = max(score, max_cycle)
    print(score)
