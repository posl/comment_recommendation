def main():
    S = input()
    if len(S) < 2:
        print("No")
        return
    if S[0].isupper() == False:
        print("No")
        return
    if S[-1].isupper() == False:
        print("No")
        return
    for i in range(1, len(S) - 1):
        if S[i].isnumeric() == False:
            print("No")
            return
    if int(S[1:-1]) >= 100000 and int(S[1:-1]) <= 999999:
        print("Yes")
    else:
        print("No")
