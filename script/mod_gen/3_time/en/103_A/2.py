def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])

if __name__ == '__main__':
    main()