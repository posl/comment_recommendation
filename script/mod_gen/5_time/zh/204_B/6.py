def main():
    num = int(input())
    nuts = list(map(int,input().split()))
    total = 0
    for i in nuts:
        if i >= 10:
            total += i - 10
    print(total)

if __name__ == '__main__':
    main()