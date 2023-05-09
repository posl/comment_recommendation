def main():
    Q=int(input())
    A=[]
    for i in range(Q):
        query=input().split()
        c=int(query[0])
        if c==1:
            A.append(int(query[1]))
        elif c==2:
            x=int(query[1])
            k=int(query[2])
            A=list(filter(lambda a:a<=x,A))
            A.sort(reverse=True)
            if len(A)>=k:
                print(A[k-1])
            else:
                print(-1)
        elif c==3:
            x=int(query[1])
            k=int(query[2])
            A=list(filter(lambda a:a>=x,A))
            A.sort()
            if len(A)>=k:
                print(A[k-1])
            else:
                print(-1)

if __name__ == '__main__':
    main()