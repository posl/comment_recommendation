def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    if k == m - 1:
                        count += 1
                else:
                    break
    print(count)

if __name__ == '__main__':
    main()