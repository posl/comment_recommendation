def main():
    N = int(input())
    # N = 254
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j <= N:
                count += 1
    print(count)

if __name__ == '__main__':
    main()