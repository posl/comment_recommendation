def main():
    s = input()
    if s.islower() or s.isupper():
        print("No")
    elif s.isalpha():
        print("Yes")
    else:
        print("No")
