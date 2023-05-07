def is_match(s, t):
    # s = s[1:] + s[0] とすると、s の先頭の文字が末尾に移動する
    # この操作を繰り返して s が t に一致するかどうかを判定する
    for _ in range(len(s)):
        if s == t:
            return True
        s = s[1:] + s[0]
    return False

if __name__ == '__main__':
    is_match()