def main():
    n,k,a = map(int, input().split())
    print(1 + (k - a - 1) // (n - a))

if __name__ == '__main__':
    main()