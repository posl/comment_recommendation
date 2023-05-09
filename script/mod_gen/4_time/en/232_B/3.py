def solve():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i:] + S[:i] == T:
            return "Yes"
    return "No"
print(solve())

if __name__ == '__main__':
    solve()