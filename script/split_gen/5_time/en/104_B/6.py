def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1:
        S = S.replace("A", "").replace("C", "")
        if S.islower():
            print("AC")
            return
    print("WA")
