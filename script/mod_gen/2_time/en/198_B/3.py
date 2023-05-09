def main():
    n = input()
    n = n[::-1]
    n = int(n)
    n = str(n)
    if n == n[::-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()