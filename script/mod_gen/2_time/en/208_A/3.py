def main():
    A, B = map(int, input().split())
    if A * 6 < B:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()