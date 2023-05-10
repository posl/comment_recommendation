def main():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    for i in range(10 ** n):
        s = str(i)
        if len(s) != n:
            continue
        for j in range(m):
            if int(s[sc[j][0] - 1]) != sc[j][1]:
                break
        else:
            print(i)
            exit()
    print(-1)

if __name__ == '__main__':
    main()