def main():
    a, b = map(int, input().split())
    if 1 <= a <= 100 and 1 <= b <= 1000:
        if a <= b <= 6*a:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()