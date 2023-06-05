def main():
    a = input()
    a = a.split()
    a = list(map(int, a))
    a.sort()
    if (a[2]-a[1])==(a[1]-a[0]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()