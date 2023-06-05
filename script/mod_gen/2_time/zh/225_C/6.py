def main():
    N = int(input())
    a = [0] * (N - 1)
    b = [0] * (N - 1)
    for i in range(N - 1):
        a[i], b[i] = map(int, input().split())
    c = [0] * N
    for i in range(N - 1):
        c[a[i] - 1] += 1
        c[b[i] - 1] += 1
    for i in range(N):
        if c[i] == N - 1:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()