def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    #print(n,k,x)
    if k == 1:
        print(0)
    else:
        #x.sort()
        #print(x)
        result = 0
        for i in range(0,k-1):
            result += x[i]
        print(result)
