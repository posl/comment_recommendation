def main():
    #入力
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    #x=0,y=0
    ans = sum(A)
    #x=0,y=1
    ans = min(ans,sum(A[:-1])+min(A[-1]*R,R))
    #x=1,y=0
    ans = min(ans,sum(A[1:])+min(A[0]*L,L))
    #x=1,y=1
    ans = min(ans,sum(A[1:-1])+min(A[0]*L,L)+min(A[-1]*R,R))
    #x=0,y=2
    ans = min(ans,sum(A[:-2])+min(A[-2]*R,R)+min(A[-1]*R,R))
    #x=2,y=0
    ans = min(ans,sum(A[2:])+min(A[0]*L,L)+min(A[1]*L,L))
    #x=1,y=2
    ans = min(ans,sum(A[1:-2])+min(A[0]*L,L)+min(A[-2]*R,R)+min(A[-1]*R,R))
    #x=2,y=1
    ans = min(ans,sum(A[2:-1])+min(A[0]*L,L)+min(A[1]*L,L)+min(A[-1]*R,R))
    #x=2,y=2
    ans = min(ans,sum(A[2:-2])+min(A[0]*L,L)+min(A[1]*L,L)+min(A[-2]*R,R)+min(A[-1]*R,R))
    #出力
    print(ans)
