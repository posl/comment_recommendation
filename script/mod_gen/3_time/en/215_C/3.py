def permute(s):
    if len(s) == 1:
        return [s]
    else:
        result = []
        for i in range(len(s)):
            for p in permute(s[:i] + s[i+1:]):
                result.append(s[i] + p)
        return result

if __name__ == '__main__':
    permute()