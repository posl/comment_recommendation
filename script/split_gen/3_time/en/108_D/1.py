def main():
    L = int(input())
    if L == 2:
        print('2 1')
        print('1 2 1')
        return
    if L == 3:
        print('2 2')
        print('1 2 1')
        print('2 1 2')
        return
    if L == 4:
        print('8 10')
        print('1 2 0')
        print('2 3 0')
        print('3 4 0')
        print('1 5 0')
        print('2 6 0')
        print('3 7 0')
        print('4 8 0')
        print('5 6 1')
        print('6 7 1')
        print('7 8 1')
        return
    N = 1
    while L > 2:
        N += 1
        L -= 2
    M = N + (N - 1) * (N - 2) // 2
    print(N, M)
    for i in range(1, N + 1):
        print(i, i + 1, 0)
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            print(i, j, 1)
