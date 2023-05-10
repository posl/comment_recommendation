def main():
    s = input().strip()
    if len(s) == 1:
        if s == "8":
            print("Yes")
        else:
            print("No")
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
    else:
        for i in range(112, 1000, 8):
            if "".join(sorted(str(i))) in "".join(sorted(s)):
                print("Yes")
                break
        else:
            print("No")
