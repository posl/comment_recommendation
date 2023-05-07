def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    board = [0, 0, 0, 0]
    for i in range(N):
        board[0] += 1
        for j in range(4):
            if board[j] > 0:
                if j + A[i] >= 4:
                    P += board[j]
                    board[j] = 0
                else:
                    board[j + A[i]] += board[j]
                    board[j] = 0
    print(P)

if __name__ == '__main__':
    main()