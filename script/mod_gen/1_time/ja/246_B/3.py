def main():
    A, B = map(int, input().split())
    if A == 0:
        print(0, 1)
    elif B == 0:
        print(1, 0)
    else:
        print(B / (A**2 + B**2)**0.5, A / (A**2 + B**2)**0.5)

if __name__ == '__main__':
    main()