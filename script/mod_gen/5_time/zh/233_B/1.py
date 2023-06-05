def reverse_string(s, l, r):
    s_list = list(s)
    s_list[l-1:r] = s_list[l-1:r][::-1]
    return ''.join(s_list)

if __name__ == '__main__':
    reverse_string()