def main():
    c1,c2,c3 = input().split()
    if c1 == c2 == c3:
        print("Won")
    else:
        print("Lost")

if __name__ == '__main__':
    main()