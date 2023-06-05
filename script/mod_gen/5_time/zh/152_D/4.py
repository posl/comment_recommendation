def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if i % 10 == i // (10 ** len(str(i)) - 1):
            count += 1
    print(count)

if __name__ == '__main__':
    main()