def main():
    a,b = map(int,input().split())
    a = str(a)*b
    b = str(b)*a
    if a<b:
        print(a)
    else:
        print(b)

if __name__ == '__main__':
    main()