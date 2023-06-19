def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    print(len([i for i in h if i >= k]))

if __name__ == '__main__':
    main()