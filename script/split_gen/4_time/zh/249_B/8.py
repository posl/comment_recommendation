def main():
    s = input()
    if s.islower() or s.isupper():
        print("No")
    elif s.islower() == False and s.isupper() == False:
        if s.isalpha() == False:
            print("No")
        else:
            if s[0].islower() and s[-1].islower():
                print("No")
            elif s[0].isupper() and s[-1].isupper():
                print("No")
            else:
                print("Yes")
