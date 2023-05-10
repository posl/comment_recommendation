def alternate(s, t):
    result = ""
    for i in range(len(s)):
        result += s[i] + t[i]
    return result

if __name__ == '__main__':
    alternate()