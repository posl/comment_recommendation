def check(S1, S2):
    if S1[0] == S1[1] == S2[0] == S2[1] == "#":
        return "No"
    elif S1[0] == S1[1] == S2[0] == S2[1] == ".":
        return "No"
    else:
        return "Yes"
S1 = input()
S2 = input()
print(check(S1, S2))

if __name__ == '__main__':
    check()