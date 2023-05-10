def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        st = input().split()
        s.append(st[0])
        t.append(int(st[1]))
    s_t = sorted(zip(s,t), key=lambda x:x[1], reverse=True)
    s_t = sorted(s_t, key=lambda x:x[0])
    print(t.index(s_t[0][1])+1)

if __name__ == '__main__':
    main()