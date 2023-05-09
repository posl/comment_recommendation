def main():
    a, b, k = map(int, input().split())
    counter = 0
    for i in range(1, max(a, b)+1):
        if a % i == 0 and b % i == 0:
            counter += 1
            if counter == k:
                print(i)
                break

if __name__ == '__main__':
    main()