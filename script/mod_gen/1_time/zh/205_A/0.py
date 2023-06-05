def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if 0 <= a and b <= 1000:
        print((a * b) / 100)

if __name__ == '__main__':
    main()