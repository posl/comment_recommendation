def main():
    D, T, S = map(int, input().split())
    if D > T * S:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()