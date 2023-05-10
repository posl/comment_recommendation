def check(s):
    if len(s) != 8:
        return False
    if s[0] < "A" or s[0] > "Z":
        return False
    if s[2:7] < "100000" or s[2:7] > "999999":
        return False
    if s[7] < "A" or s[7] > "Z":
        return False
    return True
s = input()
print("Yes" if check(s) else "No")

if __name__ == '__main__':
    check()