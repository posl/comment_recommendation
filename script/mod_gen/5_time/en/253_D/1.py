def main():
    n, a, b = map(int, input().split())
    sum = 0
    for i in range(1, n+1):
        if (i % a != 0) and (i % b != 0):
            sum += i
    print(sum)

if __name__ == '__main__':
    main()