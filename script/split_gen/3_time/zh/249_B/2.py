def main():
    s = input()
    if s.islower():
        print("No")
    elif s.isupper():
        print("No")
    elif len(s) == 1:
        print("No")
    else:
        print("Yes")
