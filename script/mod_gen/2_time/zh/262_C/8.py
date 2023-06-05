def main():
    N = 5
    M = 6
    U = [1,4,2,1,3,2]
    V = [5,5,3,4,5,5]
    #print(N, M)
    #print(U)
    #print(V)
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            if U[i] == U[j] or U[i] == V[j] or V[i] == U[j] or V[i] == V[j]:
                continue
            if (U[i], V[i]) == (U[j], V[j]) or (U[i], V[i]) == (V[j], U[j]) or (V[i], U[i]) == (U[j], V[j]) or (V[i], U[i]) == (V[j], U[j]):
                continue
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()