def main():
    N = int(input())
    a = 1
    b = 2 * N + 1
    while True:
        print(a)
        x = int(input())
        if x == 0:
            break
        elif x == a:
            a += 1
        elif x == b:
            b -= 1
        else:
            raise Exception("invalid input")

if __name__ == '__main__':
    main()