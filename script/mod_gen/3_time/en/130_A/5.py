def main():
    # Write code here
    X, A = input().split()
    X = int(X)
    A = int(A)
    if X < A:
        print("0")
    else:
        print("10")

if __name__ == '__main__':
    main()