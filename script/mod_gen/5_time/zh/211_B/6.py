def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == "H" or s1 == "2B" or s1 == "3B" or s1 == "HR":
        if s2 == "H" or s2 == "2B" or s2 == "3B" or s2 == "HR":
            if s3 == "H" or s3 == "2B" or s3 == "3B" or s3 == "HR":
                if s4 == "H" or s4 == "2B" or s4 == "3B" or s4 == "HR":
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()