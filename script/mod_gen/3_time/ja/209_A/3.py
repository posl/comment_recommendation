def main():
    a, b = map(int, input().split())
    result = 0
    for i in range(a, b+1):
        if a <= i <= b:
            result += 1
    print(result)

if __name__ == '__main__':
    main()