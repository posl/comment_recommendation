def main():
    s = input()
    t = input()
    s = list(s)
    t = list(t)
    s.sort()
    t.sort(reverse=True)
    if s < t:
        print('Yes')
    else:
        print('No')
