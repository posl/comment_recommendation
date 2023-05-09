def main():
    A, B = map(int, input().split())
    if A * 6 < B:
        print("No")
    elif A > B:
        print("No")
    else:
        print("Yes")
main()

if __name__ == '__main__':
    main()