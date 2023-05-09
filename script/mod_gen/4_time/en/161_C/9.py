def main():
    n, k = map(int, input().split())
    mod = n % k
    print(min(mod, k - mod))

if __name__ == '__main__':
    main()