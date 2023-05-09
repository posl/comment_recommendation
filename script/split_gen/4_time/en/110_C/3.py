def main():
    s = input()
    t = input()
    ss = set(s)
    tt = set(t)
    if len(ss) == len(tt):
        print('Yes')
    else:
        print('No')
