def main():
    S = input()
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[0]:
        print("Yes")
    else:
        print("No")
