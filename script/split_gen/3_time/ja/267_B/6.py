def main():
    s = input()
    if s[0] == "1" or s[-1] == "1":
        print("No")
        return
    s = s[1:-1]
    print("Yes" if "00" in s else "No")
