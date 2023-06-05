def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    #print(n,k)
    #print(a)
    #print(a[0])
    #print(a[n-1])
    #print(a[0]*a[n-1])
    if k == 1:
        print(a[0]*a[n-1])
        return
    elif k == n:
        print(1)
        return
    else:
        if a[0] == a[n-1]:
            print(1)
            return
        else:
            if a[0] == 1:
                print(1)
                return
            else:
                for i in range(2,a[0]+1):
                    #print(i)
                    if a[0]%i == 0 and a[n-1]%i == 0:
                        print(i)
                        return
                print(1)
                return
    print(1)
    return
