def get_alpha_num(s):
    alpha_num = 0
    for i in range(26):
        if chr(ord('a') + i) in s:
            alpha_num += 1
    return alpha_num

if __name__ == '__main__':
    get_alpha_num()