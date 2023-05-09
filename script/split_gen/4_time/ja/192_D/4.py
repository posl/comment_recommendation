def main():
    x = input()
    m = int(input())
    d = max([int(i) for i in x])
    if len(x) == 1:
        if int(x) <= m:
            print(1)
        else:
            print(0)
        exit()
    #print(d)
    l = d+1
    r = m+1
    while r-l > 1:
        mid = (l+r)//2
        #print(l, mid, r)
        if check(x, m, mid):
            l = mid
        else:
            r = mid
    print(l-d)
