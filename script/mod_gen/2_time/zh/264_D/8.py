def main():
    s = input()
    atcoder = 'atcoder'
    atcoder_len = len(atcoder)
    s_len = len(s)
    if s_len < atcoder_len:
        print(atcoder_len)
        return
    if s == atcoder:
        print(0)
        return
    s_index = 0
    atcoder_index = 0
    count = 0
    while s_index < s_len:
        if atcoder_index == atcoder_len:
            break
        if s[s_index] == atcoder[atcoder_index]:
            atcoder_index += 1
        else:
            count += 1
        s_index += 1
    if atcoder_index == atcoder_len:
        print(count)
    else:
        print(atcoder_len)

if __name__ == '__main__':
    main()