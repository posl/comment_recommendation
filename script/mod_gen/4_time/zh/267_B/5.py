def is_split(S):
    # 1. 1号被击倒
    # 2. 两列都有立针
    # 3. 两列之间有一列被击倒
    if S[0] == '0':
        if S[1] == '1':
            if S[2] == '0':
                return True
            else:
                return False
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    is_split()