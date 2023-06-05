def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    list = [s1,s2,s3,s4]
    if "H" in list and "2B" in list and "3B" in list and "HR" in list:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()