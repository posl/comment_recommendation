def main():
    s = input()
    t = input()
    s_set = set(s)
    t_set = set(t)
    if len(s_set) == len(t_set):
        print('Yes')
    else:
        print('No')
