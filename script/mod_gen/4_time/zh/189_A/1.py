def main():
    c_1,c_2,c_3 = input().split()
    if c_1 == c_2 and c_2 == c_3:
        print("Won")
    else:
        print("Lost")

if __name__ == '__main__':
    main()