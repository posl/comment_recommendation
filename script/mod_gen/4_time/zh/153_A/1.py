def main():
    h,a = map(int,input().split())
    if h%a==0:
        print(int(h/a))
    else:
        print(int(h/a)+1)

if __name__ == '__main__':
    main()