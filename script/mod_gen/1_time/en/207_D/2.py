def main():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    t = [list(map(int, input().split())) for _ in range(n)]
    s.sort()
    t.sort()
    for i in range(4):
        if i == 1:
            s = [[-y, x] for x, y in s]
        elif i == 2:
            s = [[-x, -y] for x, y in s]
        elif i == 3:
            s = [[y, -x] for x, y in s]
        for j in range(n):
            dx = t[0][0] - s[j][0]
            dy = t[0][1] - s[j][1]
            for k in range(n):
                s[k][0] += dx
                s[k][1] += dy
            s.sort()
            if s == t:
                print('Yes')
                return
            for k in range(n):
                s[k][0] -= dx
                s[k][1] -= dy
    print('No')
main()

if __name__ == '__main__':
    main()