def main():
    from bisect import bisect_left,bisect_right
    from heapq import heappop,heappush
    Q=int(input())
    A=[]
    for _ in range(Q):
        c,x,k=map(int,input().split())
        if c==1:
            bisect.insort(A,x)
        elif c==2:
            ans=-1
            if len(A)>=k:
                ans=A[-k]
            print(ans)
        else:
            ans=-1
            if len(A)>=k:
                ans=A[k-1]
            print(ans)
    return

if __name__ == '__main__':
    main()