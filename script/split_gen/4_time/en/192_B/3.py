def main():
    string = input()
    if string[::2].islower() and string[1::2].isupper():
        print("Yes")
    else:
        print("No")
