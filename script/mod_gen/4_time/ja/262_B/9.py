def main():
    N, M = map(int, input().split())
    if N < 3 or N > 100 or M < 1 or M > ((N*(N - 1))//2):
        print("N or M is out of range")
        return
    if M < 3:
        print(0)
        return
    graph = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        U_i, V_i = map(int, input().split())
        graph[U_i-1][V_i-1] = 1
        graph[V_i-1][U_i-1] = 1
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if graph[i][j] == 0:
                continue
            for k in range(j+1, N):
                if graph[i][k] == 1 and graph[j][k] == 1:
                    cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()