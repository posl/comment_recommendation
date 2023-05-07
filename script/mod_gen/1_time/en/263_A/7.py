def main():
    # Put your code here
    a = input().split()
    a = [int(i) for i in a]
    a.sort()
    if a[0] == a[1] == a[2] and a[3] == a[4]:
        print("Yes")
    elif a[0] == a[1] and a[2] == a[3] == a[4]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()