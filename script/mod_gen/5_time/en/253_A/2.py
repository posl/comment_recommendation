def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[1] == a[0] + a[2]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()