def main():
    n = input("Enter a 3 digit number: ")
    if n.isdigit():
        if len(n) == 3:
            if n[0] == '1' and n[1] == '1' and n[2] == '9':
                print("991")
            elif n[0] == '9' and n[1] == '1' and n[2] == '1':
                print("111")
            elif n[0] == '9' and n[1] == '1' and n[2] == '9':
                print("111")
            elif n[0] == '1' and n[1] == '9' and n[2] == '9':
                print("919")
            elif n[0] == '1' and n[1] == '9' and n[2] == '1':
                print("919")
            elif n[0] == '9' and n[1] == '9' and n[2] == '1':
                print("191")
            elif n[0] == '9' and n[1] == '9' and n[2] == '9':
                print("111")
            elif n[0] == '1' and n[1] == '9' and n[2] == '9':
                print("919")
            elif n[0] == '1' and n[1] == '1' and n[2] == '1':
                print("999")
        else:
            print("Please enter a 3 digit number")
    else:
        print("Please enter a 3 digit number")
