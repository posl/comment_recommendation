def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        N = 111 * (int(N / 111) + 1)
        print(N)
