def main():
    a,b,c,x = map(int, input().split())
    if a <= x <= b:
        print(c/b)
    else:
        print(0)
main()

if __name__ == '__main__':
    main()