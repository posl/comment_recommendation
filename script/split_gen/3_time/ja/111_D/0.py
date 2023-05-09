def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    if n == 1:
        if x[0] == 0 and y[0] == 0:
            print(0)
        else:
            print(-1)
        return
    if n == 2:
        if (x[0] + x[1]) % 2 == 0 and (y[0] + y[1]) % 2 == 0:
            print(1)
            print((abs(x[0] - x[1]) + abs(y[0] - y[1])) // 2)
        else:
            print(-1)
        return
    if n == 3:
        if (x[0] + x[1] + x[2]) % 2 == 0 and (y[0] + y[1] + y[2]) % 2 == 0:
            print(2)
            print((abs(x[0] - x[1]) + abs(y[0] - y[1])) // 2, (abs(x[0] - x[2]) + abs(y[0] - y[2])) // 2)
            for i in range(n):
                print(''.join(['R' if x[i] > 0 else 'L' for _ in range(abs(x[i]))] + ['U' if y[i] > 0 else 'D' for _ in range(abs(y[i]))]))
        else:
            print(-1)
        return
    print(3)
    print(1, 1, 2)
    for i in range(n):
        print(''.join(['R' if x[i] > 0 else 'L' for _ in range(abs(x[i]))] + ['U' if y[i] > 0 else 'D' for _ in range(abs(y[i]))]))
main()
なんかまだまだ簡単な問題であると思うのに、なかなか解けない問題だった。
まず、n=1のときは、(0, 0)にいればいいの
