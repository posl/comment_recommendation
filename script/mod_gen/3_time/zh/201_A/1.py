def main():
    a = input()
    a = a.split(" ")
    a = list(map(int,a))
    a.sort()
    if a[1] - a[0] == a[2] - a[1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()