def main():
    N,Q = map(int,input().split())
    T = []
    A = []
    B = []
    for i in range(Q):
        t,a,b = map(int,input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    follow = []
    for i in range(N):
        follow.append([])
    for i in range(Q):
        if T[i] == 1:
            follow[A[i]-1].append(B[i])
        elif T[i] == 2:
            if B[i] in follow[A[i]-1]:
                follow[A[i]-1].remove(B[i])
        else:
            if B[i] in follow[A[i]-1] and A[i] in follow[B[i]-1]:
                print('Yes')
            else:
                print('No')
