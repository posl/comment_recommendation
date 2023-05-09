def main():
    a,b = map(int,input().split())
    if a*b == 0:
        print(0)
    else:
        print(min(str(a)*b,str(b)*a))

if __name__ == '__main__':
    main()