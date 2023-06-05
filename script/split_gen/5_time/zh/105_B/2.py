def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0:
        print('Yes')
        return
    for i in range(1, N // 4 + 1):
        if (N - 4 * i) % 7 == 0:
            print('Yes')
            return
    print('No')
