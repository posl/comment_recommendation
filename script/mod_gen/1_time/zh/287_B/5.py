def main():
    n,m = map(int,input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()