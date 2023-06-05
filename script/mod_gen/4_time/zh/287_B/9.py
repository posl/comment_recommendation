def main():
    n,m = map(int,input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    count = 0
    for i in range(m):
        for j in range(n):
            if t[i] == s[j][-3:]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()