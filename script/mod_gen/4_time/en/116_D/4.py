def main():
    N,K = map(int,input().split())
    T = [0]*N
    D = [0]*N
    for i in range(N):
        t,d = map(int,input().split())
        T[i] = t
        D[i] = d
    D,T = zip(*sorted(zip(D,T),reverse=True))
    D = list(D)
    T = list(T)
    D = D[:K]
    T = T[:K]
    D.sort(reverse=True)
    T.sort()
    T.append(0)
    s = sum(D)
    x = len(set(T))
    ans = s + x*x
    for i in range(K):
        if T[i] != T[i+1]:
            s -= D[i]
            x -= 1
            if x == 0:
                break
            ans = max(ans,s+x*x)
    print(ans)

if __name__ == '__main__':
    main()