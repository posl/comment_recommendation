def solve():
    N = int(input())
    A = list(map(int,input().split()))
    A_acc = [0]
    for i in range(N):
        A_acc.append(A_acc[i]+A[i])
    #print(A_acc)
    ans = 10**9
    for i in range(1,N-2):
        for j in range(i+1,N-1):
            #print(i,j)
            P = A_acc[i]
            Q = A_acc[j]-A_acc[i]
            R = A_acc[N]-A_acc[j]
            S = A_acc[N]-A_acc[j]
            #print(P,Q,R,S)
            tmp = max(P,Q,R,S)-min(P,Q,R,S)
            if tmp < ans:
                ans = tmp
    print(ans)

if __name__ == '__main__':
    solve()