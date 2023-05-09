def main():
    s = input()
    if len(s) >= 2:
        if s.isupper():
            print("No")
        elif s.islower():
            print("No")
        elif s.isalpha():
            print("Yes")
        else:
            print("No")
    else:
        print("No")
