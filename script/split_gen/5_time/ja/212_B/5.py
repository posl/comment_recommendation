def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Weak")
    else:
        if int(s[0]) == 9 and int(s[1]) == 0 and int(s[2]) == 1 and int(s[3]) == 2:
            print("Weak")
        else:
            if (int(s[1]) - int(s[0]) + 10) % 10 == 1 and (int(s[2]) - int(s[1]) + 10) % 10 == 1 and (int(s[3]) - int(s[2]) + 10) % 10 == 1:
                print("Weak")
            else:
                print("Strong")
