def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    board = [0, 0, 0, 0]
    for i in range(N):
        board[0] += 1
        for j in range(4):
            if board[j] > 0:
                board[j] -= 1
                board[j + A[i]] += 1
        for k in range(4):
            if board[k] > 1:
                P += board[k] - 1
                board[k] = 1
    print(P)
