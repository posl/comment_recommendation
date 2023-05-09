def main():
    N, Q = map(int, input().split())
    a = [i + 1 for i in range(N)]
    b = [0] * N
    for _ in range(Q):
        x = int(input())
        b[x - 1] += 1
    for i in range(N):
        a[i] = a[i] - b[i]
    for i in range(N):
        a[i] = a[i] + b[a[i] - 1]
    print(*a)

if __name__ == '__main__':
    main()