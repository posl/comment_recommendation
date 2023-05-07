def main():
    a, b, k = map(int, input().split())
    c = 0
    for i in range(max(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            c += 1
            if c == k:
                print(i)
                break

if __name__ == '__main__':
    main()