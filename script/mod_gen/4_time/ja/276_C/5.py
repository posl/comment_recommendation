def main():
    N = int(input())
    P = list(map(int, input().split()))
    P = [0] + P
    Q = [0] * (N + 1)
    for i in range(1, N + 1):
        Q[P[i]] = i
    print(*Q[1:])

if __name__ == '__main__':
    main()