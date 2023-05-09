def main():
    a,b = map(int,input().split())
    if str(a)*b < str(b)*a:
        print(str(a)*b)
    else:
        print(str(b)*a)

if __name__ == '__main__':
    main()