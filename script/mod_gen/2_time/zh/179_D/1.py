def main():
    n,k = map(int,input().split())
    l = []
    r = []
    for i in range(k):
        li,ri = map(int,input().split())
        l.append(li)
        r.append(ri)
    #print(l)
    #print(r)
    #print(n)
    count = 0
    for i in range(k):
        for j in range(i+1,k):
            if l[i] <= l[j] and l[j] <= r[i]:
                count += 1
            elif l[i] <= r[j] and r[j] <= r[i]:
                count += 1
            elif l[j] <= l[i] and l[i] <= r[j]:
                count += 1
            elif l[j] <= r[i] and r[i] <= r[j]:
                count += 1
    print(count)
main()
