def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(10 * (5 + (max(a, b, c, d, e) - 1) // 10))

if __name__ == '__main__':
    main()