def solve(n, s, w):
    # print(n, s, w)
    # print(s.count('0'), s.count('1'))
    # print(w)
    # print(max(w), min(w))
    # print(s.count('0')*min(w), s.count('1')*max(w))
    return max(s.count('0')*min(w), s.count('1')*max(w))
