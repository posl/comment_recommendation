def main():
    a, b, c = [int(x) for x in input().split()]
    if a**2 + b**2 < c**2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()