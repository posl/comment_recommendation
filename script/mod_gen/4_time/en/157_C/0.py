def main():
    n, m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
    for i in range(10 ** (n - 1), 10 ** n):
        flag = True
        for j in range(m):
            if int(str(i)[s[j] - 1]) != c[j]:
                flag = False
        if flag:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()