def main():
    s = input()
    n = len(s)
    s_min = s
    s_max = s
    for i in range(n):
        s = s[1:] + s[0]
        if s < s_min:
            s_min = s
        if s > s_max:
            s_max = s
    print(s_min)
    print(s_max)
