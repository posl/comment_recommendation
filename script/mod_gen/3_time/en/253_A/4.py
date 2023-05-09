def main():
    a, b, c = map(int, input().split())
    if b >= a and b <= c:
        print("Yes")
    elif b >= c and b <= a:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()