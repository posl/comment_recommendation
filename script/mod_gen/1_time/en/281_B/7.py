def solve():
    S = input()
    if len(S) != 8:
        print("No")
        return
    if S[0].isupper() and S[7].isupper() and S[1:7].isdigit() and int(S[1:7]) >= 100000 and int(S[1:7]) <= 999999:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()