def main():
    S = input()
    if S[0] == "0":
        print("No")
    elif S[1:5] == "0" or S[6:] == "0":
        print("No")
    else:
        print("Yes")
