def main():
    n,m = map(int,input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    for i in range(n):
        for j in range(n):
            if i != j:
                t.append(s[i] + "_" + s[j])
    t = list(set(t))
    t.sort(key=lambda x: len(x))
    for i in t:
        if len(i) < 3:
            continue
        for j in t:
            if i == j:
                continue
            if i in j:
                break
        else:
            print(i)
            exit()
    print(-1)
main()

if __name__ == '__main__':
    main()