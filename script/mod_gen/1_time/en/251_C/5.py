def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(int(ti))
    ans = 0
    for i in range(n):
        if s[i] not in s[:i]:
            if t[i] > t[ans]:
                ans = i
    print(ans + 1)

if __name__ == '__main__':
    main()