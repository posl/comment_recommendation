def main():
    a,b = map(int,input().strip().split())
    if a < b and 1 <= a and b <= 15:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()