def main():
    s = input()
    if s[0].isupper() and s[-1].isupper():
        for i in range(1, len(s)-1):
            if s[i].isdigit():
                continue
            else:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
