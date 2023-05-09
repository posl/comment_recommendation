def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len + 1 != t_len:
        print("No")
        return
    if s == t[:-1]:
        print("Yes")
        return
    print("No")
