def solve(S, T):
    for i in range(len(S)):
        if S[i:] + S[:i] == T:
            return True
    return False

if __name__ == '__main__':
    solve()