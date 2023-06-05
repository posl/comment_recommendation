def main():
    s = input()
    if s[0] == "A":
        if s[2:-1].count("C") == 1:
            if s[1:].replace("C","").islower():
                print("AC")
                return
    print("WA")
    return
