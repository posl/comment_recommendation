def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    score = M * N - sum(A)
    if score < 0:
        print(-1)
    elif score > K:
        print(-1)
    else:
        print(score)

if __name__ == '__main__':
    main()