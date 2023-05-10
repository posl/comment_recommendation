def main():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    t = [list(map(int, input().split())) for _ in range(n)]
    s.sort()
    t.sort()
    for i in range(1, n):
        s[i][0] -= s[0][0]
        s[i][1] -= s[0][1]
        t[i][0] -= t[0][0]
        t[i][1] -= t[0][1]
    s[0][0] = s[0][1] = 0
    t[0][0] = t[0][1] = 0
    s.sort(key=lambda x: x[1] * 1000000 + x[0])
    t.sort(key=lambda x: x[1] * 1000000 + x[0])
    for i in range(n):
        s[i][0] *= 1000000
        t[i][0] *= 1000000
    for i in range(n):
        s[i][1] *= 1000000
        t[i][1] *= 1000000
    for i in range(n):
        s[i][0] = -s[i][0]
        t[i][0] = -t[i][0]
    for i in range(n):
        s[i][1] = -s[i][1]
        t[i][1] = -t[i][1]
    for i in range(n):
        s[i][0] += t[0][0]
        s[i][1] += t[0][1]
    for i in range(n):
        s[i][0] -= s[0][0]
        s[i][1] -= s[0][1]
    for i in range(n):
        s[i][0] /= 1000000
        t[i][0] /= 1000000
    for i in range(n):
        s[i][1] /= 1000000
        t[i][1] /= 1000000
    for i in range(n):
        s[i][0] += t[0][0]
        s[i][1] += t[0][1]
    for i in range(n):
        s[i][0] -= s[0][0

if __name__ == '__main__':
    main()