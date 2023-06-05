def main():
    s = input()
    if s[0] == "0":
        print("No")
        return
    if s[4] == "0" and s[5] == "0":
        print("No")
        return
    if s[6] == "0" and s[7] == "0" and s[8] == "0" and s[9] == "0":
        print("No")
        return
    print("Yes")
