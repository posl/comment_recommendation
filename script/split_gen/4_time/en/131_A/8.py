def main():
    #Take input from user
    S = input()
    #Check if the number is hard to enter
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
    else:
        print("Good")
