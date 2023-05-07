def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    #print(N, M, T)
    #print(A)
    #print(X, Y)
    #print("-----")
    #初期値
    time = T
    room = 1
    #print("time:", time, "room:", room)
    for i in range(N-1):
        #print("time:", time, "room:", room)
        time -= A[i]
        if time <= 0:
            print("No")
            return
        for j in range(M):
            if room == X[j]:
                time += Y[j]
        room += 1
    #print("time:", time, "room:", room)
    if time > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()