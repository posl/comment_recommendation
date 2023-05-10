def main():
    a, b, c = map(int, input().split())
    if a == b and a != c:
        print("Yes")
    elif b == c and b != a:
        print("Yes")
    elif c == a and c != b:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()