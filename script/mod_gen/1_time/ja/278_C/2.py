def main():
    N, Q = map(int, input().split())
    follow = [[0] * N for _ in range(N)]
    for _ in range(Q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            follow[a][b] = 1
        elif t == 2:
            follow[b][a] = 1
        else:
            if follow[a][b] == 1:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()