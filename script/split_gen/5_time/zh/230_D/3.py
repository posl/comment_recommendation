def main():
    n,d = map(int,input().split())
    lst = []
    for i in range(n):
        l,r = map(int,input().split())
        lst.append([l,r])
    lst.sort()
    #print(lst)
    if n == 1:
        print(1)
        return
    ans = 1
    l = lst[0][0]
    r = lst[0][1]
    for i in range(1,n):
        if lst[i][0] > r:
            l = lst[i][0]
            r = lst[i][1]
            ans += 1
        else:
            l = max(l,lst[i][0])
            r = min(r,lst[i][1])
    print(ans)
    return
