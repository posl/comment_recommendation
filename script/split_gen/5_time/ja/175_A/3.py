def main():
    S = input()
    if S[0] == S[1] == S[2]:
        print(0)
    elif S[0] != S[1] != S[2] != S[0]:
        print(1)
    else:
        print(2)
