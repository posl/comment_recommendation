def solve(S,T):
    i = 0
    j = 0
    while i < len(S) and j < len(T):
        if S[i] == T[j]:
            i += 1
            j += 1
        elif j > 0 and T[j] == T[j-1]:
            j += 1
        else:
            return "No"
    if i < len(S):
        return "No"
    while j < len(T):
        if T[j] != T[j-1]:
            return "No"
        j += 1
    return "Yes"
S = input()
T = input()
print(solve(S,T))

if __name__ == '__main__':
    solve()