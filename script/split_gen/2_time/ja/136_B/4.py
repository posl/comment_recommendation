def main():
    N = int(input())
    if N < 10:
        print(N)
    else:
        print(9 + (N - 9) // 2)
