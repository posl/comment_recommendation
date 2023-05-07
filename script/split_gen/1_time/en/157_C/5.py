def check(n, M, S, C):
    for i in range(M):
        if n[S[i]-1] != str(C[i]):
            return False
    return True
N, M = map(int, input().split())
S = []
C = []
for i in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)
for i in range(10**N):
    n = str(i)
    if len(n) != N:
        n = '0'*(N-len(n)) + n
    if check(n, M, S, C):
        print(n)
        exit()
print(-1)
