def main():
    a = input().split()
    a = list(map(int, a))
    a.sort()
    if a[0] == a[1] and a[1] != a[2]:
        print("Yes")
    elif a[0] != a[1] and a[1] == a[2]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()