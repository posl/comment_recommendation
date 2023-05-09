def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_, t_ = input().split()
        s.append(s_)
        t.append(t_)
    a = []
    for i in range(N):
        if s[i] in a or t[i] in a:
            print('No')
            return
        a.append(s[i])
        a.append(t[i])
    print('Yes')

if __name__ == '__main__':
    main()