def solve():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    S = input()
    #print(N)
    #print(P)
    #print(S)
    #print(type(P[0][0]))
    #print(type(P[0][1]))
    #print(type(S[0]))
    for i in range(N):
        if S[i] == 'R':
            P[i][0] += 1
        else:
            P[i][0] -= 1
    #print(P)
    P.sort()
    #print(P)
    for i in range(N-1):
        if P[i][0] == P[i+1][0] and (P[i][1] - P[i+1][1]) % 2 == 0:
            print('Yes')
            return
    print('No')
