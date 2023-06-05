def solve():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    if N<=2*K:
        if sorted(A)==A:
            print("Yes")
        else:
            print("No")
        return
    else:
        if sorted(A[:K+1])==A[:K+1] and sorted(A[K:])==A[K:]:
            print("Yes")
        else:
            print("No")
        return

if __name__ == '__main__':
    solve()