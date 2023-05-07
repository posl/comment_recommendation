def main():
    s = input()
    n = len(s)
    if s[0].isupper() and s[-1].isupper():
        for i in range(1,n-1):
            if not s[i].isdigit():
                print('No')
                return
        if 100000 <= int(s[1:-1]) <= 999999:
            print('Yes')
            return
    print('No')
    return
