def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    if h <= a[0]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()