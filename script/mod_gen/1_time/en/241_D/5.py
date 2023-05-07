def main():
    Q=int(input())
    A=[]
    for i in range(Q):
        query=input().split()
        if query[0]=='1':
            A.append(int(query[1]))
        elif query[0]=='2':
            A.sort()
            x=int(query[1])
            k=int(query[2])
            count=0
            for i in range(len(A)):
                if A[i]<=x:
                    count+=1
            if count<k:
                print(-1)
            else:
                print(A[-k])
        elif query[0]=='3':
            A.sort()
            x=int(query[1])
            k=int(query[2])
            count=0
            for i in range(len(A)):
                if A[i]>=x:
                    count+=1
            if count<k:
                print(-1)
            else:
                print(A[k-1])
main()

if __name__ == '__main__':
    main()