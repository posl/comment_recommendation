def solve(S):
    count = 0
    for i in range(len(S)):
        if S[i] == "0":
            count += 1
    return min(count, len(S)-count)*2

if __name__ == '__main__':
    solve()