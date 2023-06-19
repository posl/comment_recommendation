def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input())))
    ans = -1
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i
                nj = j
                tmp = a[ni][nj]
                for l in range(n - 1):
                    if k == 0:
                        ni += 1
                    elif k == 1:
                        ni -= 1
                    elif k == 2:
                        nj += 1
                    elif k == 3:
                        nj -= 1
                    tmp *= 10
                    tmp += a[ni][nj]
                ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()