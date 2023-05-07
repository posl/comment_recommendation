def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)
main()
This is the solution I came up with. I am not sure if it is the best way to do it, but it works.

if __name__ == '__main__':
    main()