def main():
    n, x = map(int, input().split())
    l = []
    a = []
    for i in range(n):
        l.append(list(map(int, input().split())))
        a.append(l[i][1:])
    #print(l)
    #print(a)
    count = 0
    for i in range(2**n):
        #print(i)
        tmp = []
        for j in range(n):
            if i & (1<<j):
                tmp.append(a[j])
        #print(tmp)
        if len(tmp) == 0:
            continue
        tmp2 = []
        for j in range(len(tmp)):
            tmp2.extend(tmp[j])
        #print(tmp2)
        if x == 1:
            count += 1
        else:
            if x % prod(tmp2) == 0:
                count += 1
    print(count)
main()
