def main():
    n, q = map(int, input().split())
    follow = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a-1][b-1] = 1
        elif t == 2:
            follow[a-1][b-1] = 0
        else:
            if follow[a-1][b-1] == 1:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()