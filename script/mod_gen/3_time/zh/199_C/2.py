def main():
    n = int(input())
    s = input()
    q = int(input())
    t = [0] * q
    a = [0] * q
    b = [0] * q
    for i in range(q):
        t[i], a[i], b[i] = map(int, input().split())
    # print(n, s, q, t, a, b)
    for i in range(q):
        if t[i] == 1:
            s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        else:
            s = s[n:] + s[:n]
    print(s)

if __name__ == '__main__':
    main()