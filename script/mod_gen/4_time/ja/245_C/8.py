def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    A.reverse()
    B.reverse()
    #print(A)
    #print(B)
    #print(A[0],B[0])
    if A[0] < B[0]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()