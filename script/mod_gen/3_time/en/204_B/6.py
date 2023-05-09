def main():
    n = int(input())
    nuts = [int(i) for i in input().split()]
    total = 0
    for i in nuts:
        if i > 10:
            total += i - 10
    print(total)

if __name__ == '__main__':
    main()