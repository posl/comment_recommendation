def main():
    n,k=map(int,input().split())
    a=[]
    b=[]
    for i in range(n):
        ai,bi=map(int,input().split())
        a.append(ai)
        b.append(bi)
    index=0
    while index<n and k>=a[index]:
        k+=b[index]
        index+=1
    print(k)

if __name__ == '__main__':
    main()