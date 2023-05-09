def main():
    import bisect
    Q=int(input())
    A=[]
    ans=[]
    for i in range(Q):
        query=list(map(int,input().split()))
        if query[0]==1:
            bisect.insort(A,query[1])
        elif query[0]==2:
            if len(A)<query[2]:
                ans.append(-1)
            else:
                ans.append(A[-query[2]])
        else:
            if len(A)<query[2]:
                ans.append(-1)
            else:
                ans.append(A[query[2]-1])
    print('\n'.join(map(str,ans)))
main()

if __name__ == '__main__':
    main()