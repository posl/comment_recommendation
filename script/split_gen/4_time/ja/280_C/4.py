def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(t_len):
        if s[i] != t[i]:
            print(i+1)
            return
    print(t_len+1)
