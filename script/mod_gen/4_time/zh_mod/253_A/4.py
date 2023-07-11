def main():
    a,b,c = map(int, input().split())
    if b > a and b < c:
        print("Yes")

if __name__ == '__main__':
    main()