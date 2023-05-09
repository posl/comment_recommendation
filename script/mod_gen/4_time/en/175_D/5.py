def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    max_score = -float('inf')
    for i in range(N):
        score = 0
        current = i
        for _ in range(K):
            current = P[current] - 1
            score += C[current]
            max_score = max(max_score, score)
            if current == i:
                break
    print(max_score)

if __name__ == '__main__':
    main()