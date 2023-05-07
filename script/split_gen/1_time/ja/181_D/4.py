def main():
    s = list(input())
    if len(s) == 1:
        if s[0] == "8":
            print("Yes")
        else:
            print("No")
    elif len(s) == 2:
        if int(s[0]+s[1]) % 8 == 0 or int(s[1]+s[0]) % 8 == 0:
            print("Yes")
        else:
            print("No")
    else:
        ans = "No"
        for i in range(100, 1000):
            if i % 8 == 0:
                if str(i)[0] in s and str(i)[1] in s and str(i)[2] in s:
                    ans = "Yes"
        print(ans)
