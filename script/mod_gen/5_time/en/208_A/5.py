def main():
    A, B = map(int, input().split())
    if (A <= B and B <= 6*A):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()