def main():
    s = input()
    t = input()
    ans = "Yes"
    if t[0:len(s)] != s:
        ans = "No"
    elif len(set(t)) == len(set(s)):
        ans = "No"
    print(ans)
