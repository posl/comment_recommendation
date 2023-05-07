def main():
    s = input()
    t = input()
    flag = False
    if s == t:
        flag = True
    else:
        for i in range(len(s)-1):
            s = s[:i] + s[i+1] + s[i] + s[i+2:]
            if s == t:
                flag = True
                break
            else:
                s = s[:i] + s[i+1] + s[i] + s[i+2:]
    if flag:
        print("Yes")
    else:
        print("No")
