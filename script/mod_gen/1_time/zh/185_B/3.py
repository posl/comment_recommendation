def main():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    battery = N
    for i in range(M):
        battery -= A[i] - B[i - 1]
        if battery <= 0:
            print("No")
            return
        battery += B[i] - A[i]
        if battery > N:
            battery = N
    battery -= T - B[-1]
    if battery <= 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()