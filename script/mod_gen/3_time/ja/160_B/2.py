def main():
    x = int(input())
    result = 0
    if x >= 500:
        result += (x // 500) * 1000
        x = x % 500
    if x >= 5:
        result += (x // 5) * 5
        x = x % 5
    print(result)

if __name__ == '__main__':
    main()