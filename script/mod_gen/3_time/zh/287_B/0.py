def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    #print(s)
    #print(t)
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                count += 1
    print(count)
    return 0

if __name__ == '__main__':
    main()