def main():
    s = input()
    if s[0] == "0":
        print("No")
        return
    if s[1:4] == "000" and s[4:7] == "000" and s[7:] == "000":
        print("No")
        return
    if s[1:4] == "111" and s[4:7] == "111" and s[7:] == "111":
        print("No")
        return
    print("Yes")
