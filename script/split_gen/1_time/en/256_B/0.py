def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    squares = [0, 0, 0, 0]
    squares[0] = 1
    for i in range(N):
        squares[0] += 1
        for j in range(4):
            if squares[j] > 0:
                if j + A[i] > 3:
                    P += squares[j]
                    squares[j] = 0
                else:
                    squares[j + A[i]] += squares[j]
                    squares[j] = 0
    print(P)
