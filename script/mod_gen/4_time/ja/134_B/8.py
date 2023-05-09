def main():
    n, d = map(int, input().split())
    print(1 + (n-1) // (2*d+1))

if __name__ == '__main__':
    main()