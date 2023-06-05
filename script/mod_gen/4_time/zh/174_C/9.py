def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    num = 7
    count = 1
    while num % k != 0:
        num = (num * 10 + 7) % k
        count += 1
    print(count)

if __name__ == '__main__':
    main()