def main():
    s = input()
    t = input()
    # print(s)
    # print(t)
    if len(s) == len(t):
        for i in range(len(s)-1):
            if s[i] == t[i]:
                s = s[:i+1] + s[i] + s[i+1:]
                # print(s)
                if s == t:
                    print("Yes")
                    exit()
        print("No")
    else:
        print("No")
