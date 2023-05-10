def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = 0
    for i in a:
        b += 1/i
    print(1/b)

if __name__ == '__main__':
    main()