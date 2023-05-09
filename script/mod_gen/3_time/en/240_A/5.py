def main():
    a, b = map(int,input().split())
    if a in [1,9,7,4] and b in [1,9,7,4]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()