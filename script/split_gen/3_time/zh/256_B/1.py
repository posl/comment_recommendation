def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    squares = [0 for i in range(4)]
    for i in range(N):
        squares[0] += 1
        for j in range(4):
            if squares[j] > 0:
                squares[(j + A[i]) % 4] += squares[j]
                squares[j] = 0
        P += squares[3]
    print(P)
