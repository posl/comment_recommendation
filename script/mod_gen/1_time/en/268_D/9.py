def get_permutation(s, t):
    if len(s) == 0:
        print(t)
        return
    for i in range(len(s)):
        get_permutation(s[:i] + s[i+1:], t + s[i])

if __name__ == '__main__':
    get_permutation()