def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            else:
                if s[i] == t[i+1]:
                    continue
                else:
                    print("No")
                    exit()
        print("Yes")
    else:
        print("No")
