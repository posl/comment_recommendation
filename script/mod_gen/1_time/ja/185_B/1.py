def main():
    N, M, T = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A.append(T)
    B.append(T)
    ans = "Yes"
    battery = N
    for i in range(M + 1):
        battery -= A[i] - B[i - 1]
        if battery <= 0:
            ans = "No"
            break
        if i < M:
            battery += B[i] - A[i]
            if battery > N:
                battery = N
    print(ans)

if __name__ == '__main__':
    main()