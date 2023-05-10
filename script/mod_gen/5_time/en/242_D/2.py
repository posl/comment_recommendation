def main():
    s = input()
    q = int(input())
    t = []
    k = []
    for i in range(q):
        t_i, k_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)
    for i in range(q):
        s = s * 2
        t_i = t[i]
        k_i = k[i]
        if t_i > 0:
            s = s[t_i:]
        l = len(s)
        if k_i < l:
            print(s[k_i])
        else:
            print(s[k_i % l])

if __name__ == '__main__':
    main()