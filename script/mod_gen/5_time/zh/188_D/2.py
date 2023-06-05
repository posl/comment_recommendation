def solve():
    N,C = map(int,input().split())
    A = []
    B = []
    C = []
    for i in range(N):
        a,b,c = map(int,input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    #print(A)
    #print(B)
    #print(C)

if __name__ == '__main__':
    solve()