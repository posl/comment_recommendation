def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for a, b in AB:
        total += a / b
    total /= 2
    current = 0
    for a, b in AB:
        current += a / b
        if current >= total:
            print(current - (current - total) * b / a)
            break

if __name__ == '__main__':
    main()