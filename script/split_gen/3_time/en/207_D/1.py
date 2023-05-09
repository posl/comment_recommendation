def solve():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        a,b = map(int,input().split())
        S.append((a,b))
    for i in range(N):
        c,d = map(int,input().split())
        T.append((c,d))
    S.sort()
    T.sort()
    S1 = []
    T1 = []
    for i in range(N):
        S1.append((S[i][0]-T[0][0],S[i][1]-T[0][1]))
        T1.append((T[i][0]-T[0][0],T[i][1]-T[0][1]))
    S1.sort()
    T1.sort()
    if S1 == T1:
        print("Yes")
    else:
        print("No")
