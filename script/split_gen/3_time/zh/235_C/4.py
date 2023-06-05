def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    print(a)
    for i in range(q):
        x,k = map(int,input().split())
        print("x:%d k:%d"%(x,k))
        if k > a.count(x):
            print(-1)
        else:
            count = 0
            for j in range(len(a)):
                if a[j] == x:
                    count += 1
                    if count == k:
                        print(j+1)
                        break
