def main():
    s = input()
    if s.islower() or s.isupper():
        print("No")
    else:
        if len(set(s)) == len(s):
            print("Yes")
        else:
            print("No")
