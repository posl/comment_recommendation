def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1:
        for c in S:
            if c != "A" and c != "C":
                if c.isupper():
                    print("WA")
                    return
        print("AC")
    else:
        print("WA")
