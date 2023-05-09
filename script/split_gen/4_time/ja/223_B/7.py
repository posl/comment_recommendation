def main():
    s = input()
    s = list(s)
    s_min = s
    s_max = s
    for i in range(len(s)):
        s.append(s.pop(0))
        if s < s_min:
            s_min = s
        if s > s_max:
            s_max = s
    print(''.join(s_min))
    print(''.join(s_max))
