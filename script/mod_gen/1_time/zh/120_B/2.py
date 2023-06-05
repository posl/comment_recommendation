def main():
    a, b, k = map(int, input().split())
    count = 0
    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            count += 1
            if count == k:
                print(i)
                exit()

if __name__ == '__main__':
    main()