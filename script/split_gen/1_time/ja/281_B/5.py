def main():
    S = input()
    if S[0].isupper() and S[-1].isupper():
        if len(S) == 2:
            print("Yes")
            return
        else:
            if S[1:-1].isnumeric():
                if len(S[1:-1]) == 6 and 100000 <= int(S[1:-1]) <= 999999:
                    print("Yes")
                    return
    print("No")
    return
