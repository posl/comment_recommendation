def main():
    n,k,a = map(int, input().split())
    print((k//n) + (k%n >= a))

if __name__ == '__main__':
    main()