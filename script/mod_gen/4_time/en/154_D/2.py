def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    e = [0] * N
    for i in range(N):
        e[i] = (p[i] + 1) / 2
    sum = 0
    for i in range(K):
        sum += e[i]
    max = sum
    for i in range(K, N):
        sum += e[i]
        sum -= e[i - K]
        if sum > max:
            max = sum
    print(max)

if __name__ == '__main__':
    main()