def main():
    a, b, c = map(int, input().split())
    if a == b and b == c:
        print("No")
    elif a == b and b != c:
        print("Yes")
    elif b == c and c != a:
        print("Yes")
    elif

if __name__ == '__main__':
    main()