def main():
    num = int(input())
    list = [int(i) for i in input().split()]
    x = int(input())
    sum = 0
    count = 0
    while True:
        for i in range(num):
            sum += list[i]
            count += 1
            if sum > x:
                print(count)
                return

if __name__ == '__main__':
    main()