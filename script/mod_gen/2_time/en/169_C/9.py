def main():
    a, b = input().split()
    a = int(a)
    b = int(b[:2])
    print(a * b // 100)

if __name__ == '__main__':
    main()