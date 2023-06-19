def main():
    N,D = map(int, input().split())
    num = 2 * D + 1
    if N % num == 0:
        print(int(N / num))
    else:
        print(int(N / num) + 1)
