def main():
    N, K = map(int, input().split())
    Sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        Sushi.append((t, d))
    Sushi.sort(key=lambda x: x[1], reverse=True)
    #print(Sushi)
    T = []
    D = []
    for i in range(K):
        t, d = Sushi[i]
        T.append(t)
        D.append(d)
    T.sort()
    #print(T)
    #print(D)
    ans = sum(D) + len(set(T))**2
    #print(ans)
    for i in range(K, N):
        if Sushi[i][0] in T:
            continue
        else:
            T.append(Sushi[i][0])
            D.append(Sushi[i][1])
            T.sort()
            D.sort(reverse=True)
            #print(T)
            #print(D)
            ans = max(ans, sum(D[:K]) + len(set(T))**2)
            #print(ans)
    print(ans)
main()

if __name__ == '__main__':
    main()