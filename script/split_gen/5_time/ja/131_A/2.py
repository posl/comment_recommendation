def main():
    S = input()
    if S[0] == S[1] == S[2] == S[3]:
        print("Bad")
    elif S[0] == S[1] == S[2] or S[1] == S[2] == S[3]:
        print("Bad")
    else:
        print("Good")
main()