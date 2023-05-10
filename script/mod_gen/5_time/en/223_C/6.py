def main():
    # input
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # compute
    left = 0
    right = 0
    for a, b in AB:
        left += a / b
        right += a
    # output
    print(left / 2 + right / 2)

if __name__ == '__main__':
    main()