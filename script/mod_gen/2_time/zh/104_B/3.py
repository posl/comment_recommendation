def judge(s):
    if s[0] == 'A':
        if s[2:-1].count('C') == 1:
            for i in s[1:]:
                if i.isupper():
                    return False
            return True
    return False

if __name__ == '__main__':
    judge()