def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    r = [0] * N
    c = [0] * N
    for i in range(N):
        r[i], c[i] = map(int, input().split())
    Q = int(input())
    d = [0] * Q
    l = [0] * Q
    for i in range(Q):
        d[i], l[i] = map(str, input().split())
        l[i] = int(l[i])
    r_s -= 1
    c_s -= 1
    for i in range(N):
        r[i] -= 1
        c[i] -= 1
    for i in range(Q):
        if d[i] == 'L':
            for j in range(N):
                if r[j] == r_s and c[j] == c_s - l[i]:
                    break
            else:
                c_s -= l[i]
        elif d[i] == 'R':
            for j in range(N):
                if r[j] == r_s and c[j] == c_s + l[i]:
                    break
            else:
                c_s += l[i]
        elif d[i] == 'U':
            for j in range(N):
                if r[j] == r_s - l[i] and c[j] == c_s:
                    break
            else:
                r_s -= l[i]
        else:
            for j in range(N):
                if r[j] == r_s + l[i] and c[j] == c_s:
                    break
            else:
                r_s += l[i]
        print(r_s + 1, c_s + 1)

if __name__ == '__main__':
    main()