def permute(s):
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i in range(len(s)):
            for p in permute(s[:i] + s[i+1:]):
                perms.append(s[i] + p)
        return perms

if __name__ == '__main__':
    permute()