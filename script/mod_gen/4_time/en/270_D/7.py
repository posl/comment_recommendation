def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    stone = [1] * (N+1)
    for i in range(2, N+1):
        for j in range(K):
            if i - A[j] >= 0:
                if stone[i-A[j]] == 1:
                    stone[i] = 0
                    break
    for i in range(N, 0, -1):
        if stone[i] == 0:
            for j in range(K):
                if i - A[j] >= 0:
                    stone[i-A[j]] = 1
    print(sum(stone))

if __name__ == '__main__':
    main()