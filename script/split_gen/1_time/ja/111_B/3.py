def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print(111 * (N // 111 + 1))
