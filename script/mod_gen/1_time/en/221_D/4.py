def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    D = [0] * (10**5 + 1)
    for a, b in AB:
        D[a] += 1
        D[a + b] -= 1
    for i in range(1, 10**5 + 1):
        D[i] += D[i - 1]
    print(*D[1:N + 1])

if __name__ == '__main__':
    main()