def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    for i in range(M):
        win = [-1] * (2*N)
        for j in range(N):
            a = 2*j
            b = 2*j+1
            if A[a][i] == A[b][i]:
                win[a] = 0
                win[b] = 0
            elif A[a][i] == 'G' and A[b][i] == 'C':
                win[a] = 1
                win[b] = 0
            elif A[a][i] == 'C' and A[b][i] == 'P':
                win[a] = 1
                win[b] = 0
            elif A[a][i] == 'P' and A[b][i] == 'G':
                win[a] = 1
                win[b] = 0
            else:
                win[a] = 0
                win[b] = 1
        for j in range(2*N):
            win[j] += win.count(1)
        A = [A[i] for i in sorted(range(2*N), key=lambda x: win[x], reverse=True)]
    for i in range(2*N):
        print(i+1)

if __name__ == '__main__':
    main()