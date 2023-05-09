def is_easy(s):
    for i in range(len(s)):
        if i % 2 == 0 and s[i] in ['L', 'U', 'D']:
            continue
        elif i % 2 == 1 and s[i] in ['R', 'U', 'D']:
            continue
        else:
            return False
    return True
s = input()

if __name__ == '__main__':
    is_easy()