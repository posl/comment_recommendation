def main():
    N = int(input())
    count = 0
    for i in range(1, N):
        for j in range(1, N):
            if N - i * j > 0:
                count += 1
            else:
                break
    print(count)

if __name__ == '__main__':
    main()