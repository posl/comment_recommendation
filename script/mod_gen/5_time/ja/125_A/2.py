def main():
    A, B, T = map(int, input().split())
    total = 0
    for i in range(1, T + 1):
        if i % A == 0:
            total += B
    print(total)
    return

if __name__ == '__main__':
    main()