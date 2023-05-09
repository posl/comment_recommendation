def main():
    N, Q = map(int, input().split())
    follow = [[0 for i in range(N)] for j in range(N)]
    for i in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a - 1][b - 1] = 1
        elif t == 2:
            follow[b - 1][a - 1] = 1
        else:
            for j in range(N):
                if follow[b - 1][j] == 1:
                    follow[a - 1][j] = 1
            for j in range(N):
                if follow[a - 1][j] == 1:
                    follow[j][a - 1] = 1
            if follow[a - 1][b - 1] == 1:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()