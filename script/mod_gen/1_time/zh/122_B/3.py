def solve():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            if is_acgt(sub):
                max_len = max(max_len, len(sub))
    print(max_len)

if __name__ == '__main__':
    solve()