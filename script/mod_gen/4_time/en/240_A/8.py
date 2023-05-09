def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if (b-a) == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()