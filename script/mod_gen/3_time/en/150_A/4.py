def main():
    K, X = input().split()
    K = int(K)
    X = int(X)
    if K * 500 >= X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()