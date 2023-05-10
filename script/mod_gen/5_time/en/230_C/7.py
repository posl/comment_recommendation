def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    if (p + q - 1) % 2 == 0:
        print("#" * (s - r + 1))
        for i in range(q - p - 1):
            print("#" + "." * (s - r - 1) + "#")
        print("#" * (s - r + 1))
    else:
        for i in range(q - p + 1):
            if i % 2 == 0:
                print("#" + "." * (s - r) + "#")
            else:
                print("." * (s - r + 1))

if __name__ == '__main__':
    main()