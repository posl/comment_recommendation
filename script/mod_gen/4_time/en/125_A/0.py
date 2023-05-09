def main():
    A, B, T = [int(x) for x in input().split()]
    count = 0
    for i in range(1, T + 1):
        if i % A == 0:
            count += B
    print(count)

if __name__ == '__main__':
    main()