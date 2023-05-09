def main():
    n, m = map(int, input().split())
    if m == 0:
        print(3**n)
    else:
        print(0)

if __name__ == '__main__':
    main()