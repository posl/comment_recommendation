def main():
    a,b = map(int,input().split())
    if a*b == 0:
        print(0)
        return
    if a < b:
        print(str(a)*b)
    else:
        print(str(b)*a)

if __name__ == '__main__':
    main()