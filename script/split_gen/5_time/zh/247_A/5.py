def problems247_a():
    s = input()
    print(s[1:] + '0' if s[0] == '1' else s[1:] + '1')
