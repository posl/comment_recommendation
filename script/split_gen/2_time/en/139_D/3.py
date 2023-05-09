def main():
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(N - 1 + (N - 2) * (N - 1) // 2)
