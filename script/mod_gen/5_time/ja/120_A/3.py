def main():
    a,b,c = map(int, input().split())
    if a*c <= b:
        print(c)
    else:
        print(int(b/a))

if __name__ == '__main__':
    main()