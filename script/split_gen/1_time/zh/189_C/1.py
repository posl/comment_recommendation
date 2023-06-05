def main():
    # N = 6
    # A = [2, 4, 4, 9, 4, 9]
    N = 6
    A = [200, 4, 4, 9, 4, 9]
    # N = int(input())
    # A = list(map(int, input().split()))
    max = 0
    for i in range(N):
        for j in range(i, N):
            min = 100000
            for k in range(i, j+1):
                if A[k] < min:
                    min = A[k]
            if min * (j - i + 1) > max:
                max = min * (j - i + 1)
    print(max)
