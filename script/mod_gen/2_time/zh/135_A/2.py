def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if (a+b)%2 == 0:
        print(int((a+b)/2))
    else:
        print("IMPOSIBLE")

if __name__ == '__main__':
    main()