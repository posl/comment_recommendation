def main():
    num = int(input())
    nuts = list(map(int, input().split()))
    nuts.sort()
    nuts.reverse()
    result = 0
    for i in range(num):
        if i % 2 == 0:
            result += nuts[i]
    print(result)

if __name__ == '__main__':
    main()