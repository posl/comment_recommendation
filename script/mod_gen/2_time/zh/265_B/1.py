def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for i in range(M)]
    time = T
    room = 1
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            exit()
        if room == XY[0][0]:
            time += XY[0][1]
            del XY[0]
        room += 1
    print("Yes")

if __name__ == '__main__':
    main()