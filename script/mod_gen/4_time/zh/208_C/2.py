def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    #print(a)
    #print(n,k)
    #print(a)
    #print("k//n=",k//n)
    #print("k%n=",k%n)
    for i in range(n):
        if k//n>0:
            print(k//n)
        else:
            print(0)
main()
