def main():
    N=int(input())
    A=[]
    B=[]
    C=[]
    for i in range(N):
        a,b=map(int,input().split())
        A.append(a)
        B.append(b)
        C.append(b-a)
    C.sort()
    t=0
    for i in range(N):
        t+=A[i]
        if t>C[i]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()