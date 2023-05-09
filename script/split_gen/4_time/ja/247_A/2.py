def main():
    S = input()
    print(S[1:]+"0" if S[0] == "1" else S[1:]+"1")
