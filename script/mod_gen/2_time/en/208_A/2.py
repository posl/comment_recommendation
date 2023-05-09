def main():
    A, B = map(int, input().split())
    if 6*A < B:
        print("No")
    elif B < A:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()