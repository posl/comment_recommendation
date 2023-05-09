def main():
    a, b, c = map(int, input().split())
    if a * a + b * b < c * c:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()