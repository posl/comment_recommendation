def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    D = [0] * (N + 1)
    for i in range(N):
        D[0] += AB[i][0] - 1
        D[1] += 1
        D[AB[i][1]] -= 1
    for i in range(1, N + 1):
        D[i] += D[i - 1]
    print(*D[1:])

if __name__ == '__main__':
    main()