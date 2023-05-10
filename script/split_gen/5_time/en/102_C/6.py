def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [2, 2, 3, 5, 5]
    # N = 5
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # N = 9
    # A = [6, 5, 4, 3, 2, 1]
    # N = 6
    # A = [1, 1, 1, 1, 2, 3, 4]
    # N = 7
    # print(A)
    # print(N)
    B = []
    for i in range(N):
        B.append(A[i] - (i + 1))
    # print(B)
    B.sort()
    # print(B)
    if N % 2 == 0:
        b = (B[int(N / 2) - 1] + B[int(N / 2)]) / 2
    else:
        b = B[int((N - 1) / 2)]
    # print(b)
    # print(int(b))
    # print(int(b) + 1)
    # print(int(b) - 1)
    # print(int(b) + 2)
    # print(int(b) - 2)
    # print(int(b) + 3)
    # print(int(b) - 3)
    # print(int(b) + 4)
    # print(int(b) - 4)
    # print(int(b) + 5)
    # print(int(b) - 5)
    # print(int(b) + 6)
    # print(int(b) - 6)
    # print(int(b) + 7)
    # print(int(b) - 7)
    # print(int(b) + 8)
    # print(int(b) - 8)
    # print(int(b) + 9)
    # print(int(b) - 9)
    # print(int(b) + 10)
    # print(int(b) - 10)
    # print(int(b) + 11)
    # print(int(b) - 11)
    # print(int(b) + 12)
    # print(int(b) - 12)
    #
