def main():
    N = int(input())
    A = list(map(int, input().split()))
    squares = [0, 0, 0, 0]
    P = 0
    for i in range(N):
        squares[0] += 1
        for j in range(4):
            if squares[j] != 0:
                if j + A[i] < 4:
                    squares[j + A[i]] += squares[j]
                else:
                    P += squares[j]
                squares[j] = 0
    print(P)
