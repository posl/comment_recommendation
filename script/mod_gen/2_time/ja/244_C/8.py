def main():
    n = int(input())
    a = 1
    b = 2 * n + 1
    while True:
        print(a)
        if int(input()) == 0:
            return
        a += 1
        print(b)
        if int(input()) == 0:
            return
        b -= 1
main()

if __name__ == '__main__':
    main()