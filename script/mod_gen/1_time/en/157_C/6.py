def check(n, s, c):
    return str(n)[s - 1] == str(c)
n, m = map(int, input().split())
s = [0] * m
c = [0] * m
for i in range(m):
    s[i], c[i] = map(int, input().split())

if __name__ == '__main__':
    check()