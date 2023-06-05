def main():
    a, b, c = map(int, input().split())
    if b > a and b < c or b < a and b > c:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()