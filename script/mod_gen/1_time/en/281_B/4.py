def solve(S):
    if S[0].isupper() and S[-1].isupper():
        if len(S) == 8:
            if S[1:7].isdigit():
                if int(S[1:7]) >= 100000 and int(S[1:7]) <= 999999:
                    return "Yes"
                else:
                    return "No"
            else:
                return "No"
        else:
            return "No"
    else:
        return "No"

if __name__ == '__main__':
    solve()