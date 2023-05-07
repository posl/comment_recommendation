def main():
    s = input()
    if s[0] == ')':
        print('No')
        return
    if s[-1] == '(':
        print('No')
        return
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            print('No')
            return
    if cnt == 0:
        print('Yes')
    else:
        print('No')
