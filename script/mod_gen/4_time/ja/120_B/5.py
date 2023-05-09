def main():
    a, b, k = map(int, input().split())
    i = 0
    for j in range(100, 0, -1):
        if a % j == 0 and b % j == 0:
            i += 1
            if i == k:
                print(j)
                break

if __name__ == '__main__':
    main()