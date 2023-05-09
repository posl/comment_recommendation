def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    board = [0, 0, 0, 0]
    for i in range(N):
        board[0] += 1
        for j in range(4):
            if board[j] >= 1:
                if j + A[i] < 4:
                    board[j + A[i]] += 1
                    board[j] -= 1
                else:
                    P += board[j]
                    board[j] -= board[j]
    print(P)

if __name__ == '__main__':
    main()