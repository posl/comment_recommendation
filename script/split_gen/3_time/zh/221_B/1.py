def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)-1):
            s = s[:i] + s[i+1] + s[i] + s[i+2:]
            if s == t:
                print("Yes")
                exit()
        print("No")
