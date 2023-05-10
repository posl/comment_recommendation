def main():
    # input
    s = input()
    t = input()
    # solve
    s = list(s)
    t = list(t)
    s.sort()
    t.sort(reverse=True)
    # output
    if s<t:
        print('Yes')
    else:
        print('No')
