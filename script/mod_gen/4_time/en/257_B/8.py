def move_right(pieces, i):
    if i == len(pieces):
        return pieces
    if pieces[i] == len(pieces):
        return move_right(pieces, i + 1)
    if pieces[i] < len(pieces) and pieces[i] + 1 in pieces:
        return move_right(pieces, i + 1)
    pieces[i] += 1
    return move_right(pieces, i + 1)
N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
pieces = [0] * N
for i in range(K):
    pieces[A[i] - 1] = 1
for i in range(Q):
    pieces = move_right(pieces, L[i] - 1)
for i in range(N):
    if pieces[i] == 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    move_right()