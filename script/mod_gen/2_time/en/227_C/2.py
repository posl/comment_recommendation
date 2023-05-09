def main():
    n = int(input())
    count = 0
    for a in range(1, int(n ** (1 / 3)) + 1):
        for b in range(a, int(n ** (1 / 2)) + 1):
            c = n // (a * b)
            if c < b:
                break
            count += 1
    print(count)

if __name__ == '__main__':
    main()