def solve():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0:
            if N // i < 10:
                print('Yes')
                return
    print('No')
    return
