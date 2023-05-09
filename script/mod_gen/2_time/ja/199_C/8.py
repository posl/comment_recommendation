def main():
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        t_temp, a_temp, b_temp = map(int, input().split())
        t.append(t_temp)
        a.append(a_temp)
        b.append(b_temp)
    s = list(s)
    for i in range(q):
        if t[i] == 1:
            s[a[i]-1], s[b[i]-1] = s[b[i]-1], s[a[i]-1]
        else:
            s[:n], s[n:] = s[n:], s[:n]
    print(''.join(s))

if __name__ == '__main__':
    main()