def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == "H" and s2 == "2B" and s3 == "3B" and s4 == "HR":
        print("Yes")
    elif s1 == "2B" and s2 == "3B" and s3 == "HR" and s4 == "3B":
        print("Yes")
    elif s1 == "3B" and s2 == "HR" and s3 == "3B" and s4 == "HR":
        print("Yes")
    elif s1 == "HR" and s2 == "3B" and s3 == "HR" and s4 == "3B":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()