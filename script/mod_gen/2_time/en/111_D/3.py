def main():
    n = int(input())
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    if n == 1:
        if x[0] == 0 and y[0] == 0:
            print(0)
        else:
            print(1)
            print(abs(x[0]) + abs(y[0]))
            print('U' * (y[0] > 0) + 'D' * (y[0] < 0) + 'R' * (x[0] > 0) + 'L' * (x[0] < 0))
        return
    if n == 2:
        if (x[0] + x[1]) % 2 == 0 and (y[0] + y[1]) % 2 == 0:
            print(2)
            print(abs(x[0] - x[1]) // 2 + abs(y[0] - y[1]) // 2, abs(x[0] - x[1]) // 2 + abs(y[0] - y[1]) // 2)
            print('U' * (y[0] > 0) + 'D' * (y[0] < 0) + 'R' * (x[0] > 0) + 'L' * (x[0] < 0) + \
                'U' * (y[1] > 0) + 'D' * (y[1] < 0) + 'R' * (x[1] > 0) + 'L' * (x[1] < 0))
        else:
            print(3)
            print(abs(x[0] - x[1]) + abs(y[0] - y[1]), abs(x[0] - x[1]) + abs(y[0] - y[1]), 1)
            print('U' * (y[0] > 0) + 'D' * (y[0] < 0) + 'R' * (x[0] > 0) + 'L' * (x[0] < 0) + \
                'U' * (y[

if __name__ == '__main__':
    main()