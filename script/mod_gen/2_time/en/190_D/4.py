def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            if N / i % 2 == 1:
                count += 1
    print(count * 2)

if __name__ == '__main__':
    main()