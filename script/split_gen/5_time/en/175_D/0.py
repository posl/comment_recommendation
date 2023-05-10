def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [x - 1 for x in P]
    max_score = -10**18
    for i in range(N):
        score = 0
        pos = i
        for j in range(K):
            pos = P[pos]
            score += C[pos]
            max_score = max(max_score, score)
            if pos == i:
                break
    print(max_score)
