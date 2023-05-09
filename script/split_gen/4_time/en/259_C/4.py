def main():
    s = input()
    t = input()
    s_count = {}
    t_count = {}
    for ch in s:
        if ch in s_count:
            s_count[ch] += 1
        else:
            s_count[ch] = 1
    for ch in t:
        if ch in t_count:
            t_count[ch] += 1
        else:
            t_count[ch] = 1
    if s_count == t_count:
        print('Yes')
    else:
        print('No')
