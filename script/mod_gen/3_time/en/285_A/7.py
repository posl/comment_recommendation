def main():
    a, b = map(int, input().split())
    if b-a == 1 or b-a == 2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()