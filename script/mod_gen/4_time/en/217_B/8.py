def solve(S_1, S_2, S_3):
    if S_1 == "ABC":
        if S_2 == "ARC":
            return "AGC"
        elif S_2 == "AGC":
            return "ARC"
    elif S_1 == "ARC":
        if S_2 == "ABC":
            return "AGC"
        elif S_2 == "AGC":
            return "ABC"
    elif S_1 == "AGC":
        if S_2 == "ABC":
            return "ARC"
        elif S_2 == "ARC":
            return "ABC"
S_1 = input()
S_2 = input()
S_3 = input()
print(solve(S_1, S_2, S_3))

if __name__ == '__main__':
    solve()