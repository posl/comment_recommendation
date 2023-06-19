def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].islower():
                continue
            else:
                print("No")
                break
        else:
            if s[i].isupper():
                continue
            else:
                print("No")
                break
    else:
        print("Yes")
