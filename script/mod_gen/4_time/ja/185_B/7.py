def main():
    N,M,T = map(int,input().split())
    A_B = [list(map(int,input().split())) for _ in range(M)]
    now = 0
    for i in range(M):
        if i == 0:
            now = A_B[i][0]
        else:
            now = A_B[i][0] - A_B[i-1][1]
        N += now
        if N > 100:
            N = 100
        N -= A_B[i][1] - A_B[i][0]
        if N <= 0:
            print("No")
            return
    N += T - A_B[M-1][1]
    if N > 100:
        N = 100
    if N <= 0:
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()