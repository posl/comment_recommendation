def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    a = list(map(lambda x:x-1,a))
    #print(a)
    count = 0
    for i in range(n):
        if a[i] != -1:
            count += 1
            p = a[i]
            a[i] = -1
            while a[p] != -1:
                q = a[p]
                a[p] = -1
                p = q
    print(count)
