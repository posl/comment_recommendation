def main():
    N, M = map(int, input().split())
    U = []
    V = []
    for i in range(M):
        u, v = map(int, input().split())
        U.append(u)
        V.append(v)
    #print(U)
    #print(V)
    ans = 0
    for i in range(M):
        u = U[i]
        v = V[i]
        u_set = set()
        v_set = set()
        for j in range(M):
            if i == j:
                continue
            if U[j] == u:
                u_set.add(V[j])
            if V[j] == u:
                u_set.add(U[j])
            if U[j] == v:
                v_set.add(V[j])
            if V[j] == v:
                v_set.add(U[j])
        #print(u_set)
        #print(v_set)
        ans += len(u_set & v_set)
    print(ans//3)
