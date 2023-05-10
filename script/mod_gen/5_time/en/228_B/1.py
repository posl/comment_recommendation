def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    print(len(set(a)))

if __name__ == '__main__':
    main()