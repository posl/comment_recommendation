def main():
    X = int(input())
    if X % 100 == 0 and X >= 100:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()