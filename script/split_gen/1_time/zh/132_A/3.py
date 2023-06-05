def main():
    s = input()
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    if len(d) == 2:
        for v in d.values():
            if v != 2:
                print('No')
                return
        print('Yes')
    else:
        print('No')
