def main():
    n, m = map(int, input().split())
    l = []
    for i in range(m):
        l.append(list(map(int, input().split())))
    l.sort(key=lambda x: x[1])
    ans = 0
    end = 0
    for i in range(m):
        if end < l[i][0]:
            ans += 1
            end = l[i][1]
    print(ans)

if __name__ == '__main__':
    main()