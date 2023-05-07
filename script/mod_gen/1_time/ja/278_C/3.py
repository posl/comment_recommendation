def main():
    n, q = map(int, input().split())
    follow = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a][b] = 1
        elif t == 2:
            follow[b][a] = 1
        else:
            ans = 'No'
            for i in range(1, n + 1):
                if follow[a][i] and follow[i][b]:
                    ans = 'Yes'
                    break
            print(ans)

if __name__ == '__main__':
    main()