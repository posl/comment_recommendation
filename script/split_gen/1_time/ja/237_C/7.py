def main():
    s = input()
    s_rev = s[::-1]
    if s == s_rev:
        print('Yes')
    else:
        print('No')
