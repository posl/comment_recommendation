def main():
    N = int(input())
    if N == 0:
        print(1)
    else:
        print(N * main(N-1))
