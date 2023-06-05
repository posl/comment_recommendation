def judge(s):
    if s[0] != 'A':
        return False
    if s[1] != s[-1] != 'C':
        return False
    if s[2:-1].count('C') != 1:
        return False
    for i in s[2:-1]:
        if i != i.lower():
            return False
    return True

if __name__ == '__main__':
    judge()