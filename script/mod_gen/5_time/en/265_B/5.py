def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    B = [list(map(int, input().split())) for i in range(M)]
    flag = True
    time = T
    for i in range(0, N-1):
        if time <= 0:
            flag = False
            break
        time -= A[i]
        if time > 0:
            time += B[i][1]
        else:
            time = B[i][1]
        if time > T:
            time = T
    if flag:
        if time > 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()