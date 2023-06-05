def solve():
    N,M = map(int,input().split())
    A = []
    for i in range(1,M+1):
        A.append(i)
    print(A)
    for i in range(1,M+1):
        for j in range(i+1,M+1):
            print(i,j)
            if j-i == N-1:
                print(i,j)
                break
solve()
