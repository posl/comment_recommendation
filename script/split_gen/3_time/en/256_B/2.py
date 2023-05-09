def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    square = [0, 0, 0, 0]
    for i in range(N):
        square[0] += 1
        for j in range(4):
            if square[j] > 0:
                if j + A[i] < 4:
                    square[j + A[i]] += 1
                    square[j] = 0
                else:
                    P += square[j]
                    square[j] = 0
    print(P)
