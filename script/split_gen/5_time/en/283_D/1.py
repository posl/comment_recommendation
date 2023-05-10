def main():
    s = input()
    if s[0] == ')':
        print('No')
        return
    if s[-1] == '(':
        print('No')
        return
    if s.count('(') != s.count(')'):
        print('No')
        return
    print('Yes')
    return
