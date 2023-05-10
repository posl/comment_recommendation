def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    max = -float('inf')
    for i in range(N):
        score = 0
        next = i
        for j in range(K):
            score += C[next]
            next = P[next] - 1
            if score > max:
                max = score
        if score > max:
            max = score
    print(max)

if __name__ == '__main__':
    main()