def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    print(len([x for x in h if x >= k]))

if __name__ == '__main__':
    main()