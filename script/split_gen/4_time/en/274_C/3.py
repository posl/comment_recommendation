def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 ** (N + 1))
    for i in range(N):
        B[A[i]] = i + 1
    for i in range(1, 2 ** (N + 1)):
        if B[i] != 0:
            print(0)
        else:
            j = i
            while B[j] == 0:
                j //= 2
            print(B[j])
