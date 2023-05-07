def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    #print(N, X)
    #print(L)
    D = [0]
    for i in range(N):
        D.append(D[i]+L[i])
    #print(D)
    cnt = 0
    for i in range(N+1):
        if D[i] <= X:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()