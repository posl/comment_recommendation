def main():
    N, M = map(int, input().split())
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    print(N, M)
    print(u)
    print(v)

if __name__ == '__main__':
    main()