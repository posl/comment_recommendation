def main():
    N = int(input())
    count = 0
    for i in range(1, N):
        count += (N - 1) // i
    print(count)

if __name__ == '__main__':
    main()