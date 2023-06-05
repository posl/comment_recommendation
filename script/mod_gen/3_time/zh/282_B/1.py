def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            flag = True
            for k in range(m):
                if s[i][k] == 'x' and s[j][k] == 'x':
                    flag = False
                    break
            if flag:
                count += 1
    print(count)

if __name__ == '__main__':
    main()