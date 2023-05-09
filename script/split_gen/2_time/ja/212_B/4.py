def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print("Weak")
        return
    for i in range(3):
        if int(s[i+1]) != (int(s[i])+1)%10:
            print("Strong")
            return
    print("Weak")
    return
