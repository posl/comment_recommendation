def main():
    A, B = map(int, input().split())
    if (A+B)%2 == 0:
        print((A+B)//2)
    else:
        print("IMPOSIBLE")

if __name__ == '__main__':
    main()