def f1():
    h, w, r_s, c_s = map(int, input().split())
    n = int(input())
    r = [0] * n
    c = [0] * n
    for i in range(n):
        r[i], c[i] = map(int, input().split())
    q = int(input())
    d = [0] * q
    l = [0] * q
    for i in range(q):
        d[i], l[i] = input().split()
        l[i] = int(l[i])
    # print(h, w, r_s, c_s)
    # print(n)
    # print(r)
    # print(c)
    # print(q)
    # print(d)
    # print(l)
    for i in range(q):
        if d[i] == 'L':
            c_s -= l[i]
            for j in range(n):
                if r[j] == r_s and c[j] <= c_s and c[j] >= c_s - l[i]:
                    c_s = c[j] - 1
                    break
        elif d[i] == 'R':
            c_s += l[i]
            for j in range(n):
                if r[j] == r_s and c[j] >= c_s and c[j] <= c_s + l[i]:
                    c_s = c[j] + 1
                    break
        elif d[i] == 'U':
            r_s -= l[i]
            for j in range(n):
                if c[j] == c_s and r[j] <= r_s and r[j] >= r_s - l[i]:
                    r_s = r[j] - 1
                    break
        elif d[i] == 'D':
            r_s += l[i]
            for j in range(n):
                if c[j] == c_s and r[j] >= r_s and r[j] <= r_s + l[i]:
                    r_s = r[j] + 1
                    break
        print(r_s, c_s)

if __name__ == '__main__':
    f1()