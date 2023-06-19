def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    #print(A)
    S = sum(A)
    #print(S)
    min_diff = S
    for i in range(1, N):
        #print(i)
        for j in range(i+1, N):
            #print(j)
            for k in range(j+1, N):
                #print(k)
                P = sum(A[0:i])
                Q = sum(A[i:j])
                R = sum(A[j:k])
                S = sum(A[k:])
                #print(P, Q, R, S)
                min_diff = min(min_diff, max(P, Q, R, S) - min(P, Q, R, S))
    print(min_diff)

if __name__ == '__main__':
    solve()