def main():
    X = int(input())
    print("Yes" if X % 100 == 0 and X >= 100 else "No")

if __name__ == '__main__':
    main()