def solve():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input())))
    #print(A)
    #print(A[2][3])
    max = 0
    for i in range(N):
        for j in range(N):
            #print(i, j)
            for k in range(4):
                #print(k)
                #pr

if __name__ == '__main__':
    solve()