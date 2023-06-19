def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[1]-a[0] + a[2]-a[1])
    return

if __name__ == '__main__':
    main()