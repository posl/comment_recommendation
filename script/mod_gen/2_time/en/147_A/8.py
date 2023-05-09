def main():
    a, b, c = map(int, input().split())
    print("bust" if a+b+c>=22 else "win")

if __name__ == '__main__':
    main()