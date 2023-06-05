def main():
    a = input()
    a = a.split(" ")
    a[0] = int(a[0])
    a[1] = int(a[1])
    a[2] = int(a[2])
    if (a[0] + a[1] + a[2] >= 22):
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()