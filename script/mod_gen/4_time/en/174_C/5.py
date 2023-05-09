def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    count = 0
    mod = 7 % k
    while mod != 0:
        mod = (mod * 10 + 7) % k
        count += 1
    print(count + 1)

if __name__ == '__main__':
    main()