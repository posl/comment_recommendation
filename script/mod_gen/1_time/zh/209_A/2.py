def main():
    a, b = map(int, input().split())
    count = 0
    for i in range(a, b + 1):
        count += 1
    print(count)

if __name__ == '__main__':
    main()