def main():
    n, q = map(int, input().split())
    follow = [[False for i in range(n)] for j in range(n)]
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a-1][b-1] = True
        elif t == 2:
            follow[a-1][b-1] = False
        else:
            if follow[a-1][b-1]:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()