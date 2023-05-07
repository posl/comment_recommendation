def main():
    N = input()
    N = list(map(int, N))
    N = N[::-1]
    N = sum(N)
    if N % 3 == 0:
        print(0)
    else:
        print(1)
