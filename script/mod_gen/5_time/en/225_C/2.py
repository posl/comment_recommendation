def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    A = [[(i-1)*7 + j for j in range(1, 8)] for i in range(1, 10**2+1)]
    for i in range(10**2-N+1):
        for j in range(7-M+1):
            if [A[i+k][j:j+M] for k in range(N)] == B:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()