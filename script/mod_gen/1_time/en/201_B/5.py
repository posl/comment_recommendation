def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(int(ti))
    t_max = max(t)
    t.remove(t_max)
    s_max = s[t.index(max(t))]
    print(s_max)

if __name__ == '__main__':
    main()