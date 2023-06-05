def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    squares = [0] * 4
    for i in range(n):
        squares[0] += 1
        for j in range(4):
            if squares[j] > 0:
                squares[j] -= 1
                if j + a[i] < 4:
                    squares[j + a[i]] += 1
                else:
                    p += 1
    print(p)

if __name__ == '__main__':
    main()