def main():
    s = input()
    if s[0] != "A":
        print("WA")
        return
    if s[2:-1].count("C") != 1:
        print("WA")
        return
    if s[1:].replace("C", "").islower() == False:
        print("WA")
        return
    print("AC")
