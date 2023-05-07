def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    #print(N, M, T)
    #print(A)
    #print(X)
    #print(Y)
    now = 0
    time = T
    for i in range(N-1):
        #print("now:%d time:%d" % (now, time))
        time -= A[i]
        if time <= 0:
            print("No")
            return
        for j in range(M):
            if X[j] == now+1:
                time += Y[j]
        now += 1
    print("Yes")
    return
main()

if __name__ == '__main__':
    main()