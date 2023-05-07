def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    if n != m:
        print('No')
        return
    for i in range(n):
        if s[i] != t[i]:
            if s[i+1:] != t[i+1:]:
                print('No')
                return
    print('Yes')
