def main():
    # read input
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    # compute sum of A
    A_sum = sum(A)
    # compute required score
    required_score = N * M - A_sum
    # check if required_score is achievable
    if required_score > K:
        print(-1)
    elif required_score > 0:
        print(required_score)
    else:
        print(0)

if __name__ == '__main__':
    main()