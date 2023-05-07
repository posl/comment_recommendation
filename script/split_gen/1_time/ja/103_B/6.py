def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)-1):
            s = s[len(s)-1] + s[:len(s)-1]
            if s == t:
                print("Yes")
                return
        print("No")
        return
