def main():
    N, Q = map(int, input().split())
    train = [i for i in range(N+1)]
    for i in range(Q):
        c, x, y = map(int, input().split())
        if c == 1:
            train[y] = x
        elif c == 2:
            train[x] = y
        else:
            ans = []
            while x != 0:
                ans.append(x)
                x = train[x]
            print(len(ans), *ans)
main()

if __name__ == '__main__':
    main()