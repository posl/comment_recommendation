def main():
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    d = (a**2 + b**2)**(1/2)
    print(a/d, b/d)

if __name__ == '__main__':
    main()