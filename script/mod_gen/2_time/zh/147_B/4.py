def solve(s):
    l = len(s)
    count = 0
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            count += 1
    return count

if __name__ == '__main__':
    solve()