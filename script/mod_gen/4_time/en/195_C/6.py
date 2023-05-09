def main():
    N = int(input())
    count = 0
    for i in range(1, len(str(N))+1):
        if i % 3 == 0:
            count += N - (10 ** i - 1) + 1
    print(count)
main()

if __name__ == '__main__':
    main()