def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a*b)

if __name__ == '__main__':
    main()