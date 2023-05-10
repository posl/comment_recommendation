def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    L.sort(key=lambda x: x[0])
    #print(L)
    #print(N, X)
    ans = 0
    for i in range(N):
        for j in range(L[i][0]):
            if X % L[i][1+j] == 0:
                #print(L[i][1+j])
                if i == N-1:
                    ans += 1
                else:
                    X = X // L[i][1+j]
    print(ans)
    return

if __name__ == '__main__':
    main()