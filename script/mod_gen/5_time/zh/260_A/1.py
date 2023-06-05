def solution(s):
    if s[0] == s[1] and s[1] == s[2]:
        return -1
    elif s[0] == s[1]:
        return s[2]
    elif s[1] == s[2]:
        return s[0]
    elif s[0] == s[2]:
        return s[1]
    else:
        return -1

if __name__ == '__main__':
    solution()