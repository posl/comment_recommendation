def main():
    N = int(input())
    if N % 100 == 0:
        print(int(N / 100))
    else:
        print(int(N / 100) + 1)
