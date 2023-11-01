def main():
    a, b, c = map(int, input().split())
    if a == b:
        if a != c:
            print("Yes")
        else:
            print("No")
    elif a == c:
        if a != b:

if __name__ == '__main__':
    main()