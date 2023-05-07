def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x:x[0])
    B = [0] * (M+1)
    for i in range(N):
        for j in range(M, AB[i][0]-1, -1):
            B[j] = max(B[j], B[j-AB[i][0]] + AB[i][1])
    print(B[M])

if __name__ == '__main__':
    main()