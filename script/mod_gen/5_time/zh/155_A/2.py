def main():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print("是")
    elif b == c and c != a:
        print("是")
    elif a == c and c != b:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()