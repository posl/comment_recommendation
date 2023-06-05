def main():
    n = int(input())
    u = [0] * (n - 1)
    v = [0] * (n - 1)
    w = [0] * (n - 1)
    for i in range(n - 1):
        u[i], v[i], w[i] = map(int, input().split())
    print(solve(n, u, v, w))

if __name__ == '__main__':
    main()