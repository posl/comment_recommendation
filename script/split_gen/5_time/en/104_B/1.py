def main():
    s = input()
    if s[0] != "A":
        print("WA")
        return
    if s[2:-1].count("C") != 1:
        print("WA")
        return
    for c in s:
        if c not in "AC":
            if c.isupper():
                print("WA")
                return
    print("AC")
