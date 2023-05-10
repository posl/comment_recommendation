def main():
    n, k = map(int, input().split())
    print(min(n%k, k-n%k))
main()

if __name__ == '__main__':
    main()