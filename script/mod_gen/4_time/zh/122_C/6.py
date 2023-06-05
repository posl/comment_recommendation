def solve(S, l, r):
    count = 0
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            if S[i:j] == "AC":
                count += 1
    return count

if __name__ == '__main__':
    solve()