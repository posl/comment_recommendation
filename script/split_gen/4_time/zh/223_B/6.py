def main():
    s = input()
    l = len(s)
    s = s + s
    s_min = s[0:l]
    s_max = s[0:l]
    for i in range(1, l):
        s_min = min(s_min, s[i:i+l])
        s_max = max(s_max, s[i:i+l])
    print(s_min)
    print(s_max)
