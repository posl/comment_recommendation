def lex_compare(s1, s2):
    for i in range(min(len(s1), len(s2))):
        if s1[i] < s2[i]:
            return True
        elif s1[i] > s2[i]:
            return False
    if len(s1) < len(s2):
        return True
    return False

if __name__ == '__main__':
    lex_compare()