def main():
    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort()
    left = lr[0][0]
    right = lr[0][1]
    for i in range(1, n):
        if right < lr[i][0]:
            print(left, right)
            left = lr[i][0]
            right = lr[i][1]
        else:
            if right < lr[i][1]:
                right = lr[i][1]
    print(left, right)

if __name__ == '__main__':
    main()