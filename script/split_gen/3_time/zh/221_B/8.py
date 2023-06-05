def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)-1):
            s = list(s)
            s[i], s[i+1] = s[i+1], s[i]
            s = "".join(s)
            if s == t:
                print("Yes")
                break
            else:
                s = list(s)
                s[i], s[i+1] = s[i+1], s[i]
                s = "".join(s)
        else:
            print("No")
