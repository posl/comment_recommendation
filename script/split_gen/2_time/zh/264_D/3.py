def check_atcoder(s):
    atcoder = "atcoder"
    for i in range(len(s)):
        if s[i] == atcoder[i]:
            continue
        elif s[i] > atcoder[i]:
            return False
        else:
            return True
    return False
