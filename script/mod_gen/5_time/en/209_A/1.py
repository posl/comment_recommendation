def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if (a >= 1 and a <= 100) and (b >= 1 and b <= 100):
        if a <= b:
            print(b - a + 1)
        else:
            print(0)

if __name__ == '__main__':
    main()