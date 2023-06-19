def replace(s):
    s = list(s)
    for i in range(len(s)):
        if i%2 == 1:
            s[i] = "."
    return "".join(s)

if __name__ == '__main__':
    replace()