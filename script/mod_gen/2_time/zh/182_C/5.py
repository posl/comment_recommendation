def main():
    n = input()
    k = len(n)
    n = int(n)
    for i in range(k):
        if n % 3 == 0:
            print(i)
            return
        n //= 10
    print(-1)

if __name__ == '__main__':
    main()