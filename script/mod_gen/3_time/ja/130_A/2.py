def main():
    X, A = map(int, input().split())
    if X < A:
        print("0")
    elif X >= A:
        print("10")

if __name__ == '__main__':
    main()