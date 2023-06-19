def main():
    n = int(input())
    if n >= 0 and n <= 10 ** 18:
        for i in range(n, n + 10):
            for j in range(n, n + 10):
                if i ** 3 + i ** 2 * j + i * j ** 2 + j ** 3 == n:
                    print(i)
                    return
        print(n)
        return
    else:
        return

if __name__ == '__main__':
    main()