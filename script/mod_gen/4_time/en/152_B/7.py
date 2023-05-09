def main():
    a,b = input().split()
    if a*b > b*a:
        print(b*a)
    else:
        print(a*b)

if __name__ == '__main__':
    main()