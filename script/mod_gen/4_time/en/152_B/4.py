def main():
    a, b = input().split()
    if int(a+b) < int(b+a):
        print(a*b)
    else:
        print(b*a)

if __name__ == '__main__':
    main()