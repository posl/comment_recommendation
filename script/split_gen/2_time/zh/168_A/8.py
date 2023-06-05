def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    while (K > 0):
        K -= 1
        i = A[i] - 1
        if (i == 0):
            print(1)
            return
    print(i + 1)
