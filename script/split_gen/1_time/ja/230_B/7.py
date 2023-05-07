def main():
    s = input()
    t = "o" + "x" * 10**5
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        else:
            print("No")
            return
    print("Yes")
    return
