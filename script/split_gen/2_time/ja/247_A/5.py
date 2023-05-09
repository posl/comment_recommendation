def main():
    s = input()
    ans = ""
    for i in range(0, len(s)):
        if i == len(s) - 1:
            break
        if s[i] == "1":
            ans += "1"
        else:
            ans += "0"
    if s[len(s) - 1] == "1":
        ans += "0"
    else:
        ans += "0"
    print(ans)
