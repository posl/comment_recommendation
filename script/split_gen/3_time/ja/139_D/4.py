def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    if N % 2 == 0:
        print(N // 2 - 1)
        return
    else:
        print(N // 2)
