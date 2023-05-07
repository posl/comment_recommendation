def main():
    N = int(input())
    A = list(map(int, input().split()))
    dist = [0] * (2 ** (N + 1))
    for i in range(N):
        dist[A[i]] = 1
    for i in range(1, 2 ** (N + 1)):
        if dist[i] == 0:
            dist[i] = dist[i // 2] + 1
    print('
'.join(map(str, dist[1:])))

if __name__ == '__main__':
    main()