def main():
    S = input()
    if S[0] == S[1]:
        if S[1] == S[2]:
            print(1)
        else:
            print(2)
    elif S[0] == S[2]:
        print(2)
    elif S[1] == S[2]:
        print(2)
    else:
        print(3)
