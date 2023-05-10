def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return
    if k == 1 or k == 7:
        print(1)
        return
    n = 7
    for i in range(2, k):
        n = (n * 10 + 7) % k
        if n == 0:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()