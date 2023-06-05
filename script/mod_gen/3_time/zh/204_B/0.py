def main():
    num = int(input())
    nuts = input().split()
    nuts = list(map(int, nuts))
    count = 0
    for i in range(num):
        if nuts[i] > 10:
            count += nuts[i] - 10
    print(count)

if __name__ == '__main__':
    main()