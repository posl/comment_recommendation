def main():
    a = input()
    b = input()
    c = input()
    d = input()
    if a == "H" or a == "2B" or a == "3B" or a == "HR":
        if b == "H" or b == "2B" or b == "3B" or b == "HR":
            if c == "H" or c == "2B" or c == "3B" or c == "HR":
                if d == "H" or d == "2B" or d == "3B" or d == "HR":
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
main()
