def main():
    S = input()
    #print(S)
    if S[0].isupper():
        if S[-1].isupper():
            if S[1:-1].isdecimal():
                if 100000 <= int(S[1:-1]) <= 999999:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
