def solve():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            return "No"
    return "Yes"
print(solve())

if __name__ == '__main__':
    solve()