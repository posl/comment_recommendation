def main():
    a, b = map(int, input().split())
    sum = 0
    for i in range(1, 1000):
        sum += i
        if sum - a == b - sum:
            print(sum - a)
            exit()

if __name__ == '__main__':
    main()