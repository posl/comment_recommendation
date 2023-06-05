def main():
    n,k = map(int,input().split())
    td = []
    for i in range(n):
        td.append(list(map(int,input().split())))
    td.sort(key=lambda x:x[1],reverse=True)
    td.sort(key=lambda x:x[0])
    print(td)
    t = []
    d = []
    for i in range(n):
        t.append(td[i][0])
        d.append(td[i][1])
    print(t)
    print(d)
    print()
    count = 0
    for i in range(k):
        count += d[i]
    print(count)
    print()
    count2 = 0
    for i in range(k):
        if t[i] not in t[:i]:
            count2 += 1
    print(count2)
    print()
    count3 = count + count2**2
    print(count3)
    print()
main()
