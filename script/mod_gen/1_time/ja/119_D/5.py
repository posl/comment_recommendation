def main():
    A,B,Q=map(int,input().split())
    S=[int(input())for _ in range(A)]
    T=[int(input())for _ in range(B)]
    X=[int(input())for _ in range(Q)]
    from bisect import bisect_left,bisect_right
    for x in X:
        s=S[bisect_left(S,x)]
        t=T[bisect_left(T,x)]
        sl=s-x if bisect_left(S,x)>0 else float('inf')
        sr=x-s if bisect_left(S,x)<A else float('inf')
        tl=t-x if bisect_left(T,x)>0 else float('inf')
        tr=x-t if bisect_left(T,x)<B else float('inf')
        print(min(max(sl,tl),max(sr,tr),sl+tr+min(sl,tr),sr+tl+min(sr,tl)))
main()

if __name__ == '__main__':
    main()