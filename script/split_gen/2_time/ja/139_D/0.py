def main():
    N = int(input())
    if N % 2 == 0:
        print(N * (N - 1) // 2)
    else:
        print(N * (N - 1) // 2 + 1)
