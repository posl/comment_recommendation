def permutations(s):
    if len(s) <= 1:
        yield s
    else:
        for i in range(len(s)):
            for j in permutations(s[:i] + s[i+1:]):
                yield s[i] + j

if __name__ == '__main__':
    permutations()