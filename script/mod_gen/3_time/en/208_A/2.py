def main():
    a, b = map(int, input().split())
    if 1 <= a <= 100 and 1 <= b <= 1000:
        if a*1 <= b <= a*6:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()