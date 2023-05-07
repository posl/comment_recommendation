def main():
    s = input()
    box = []
    for i in range(len(s)):
        if s[i] == '(':
            box.append(s[i])
        elif s[i] == ')':
            if len(box) == 0:
                print('No')
                return
            else:
                box.pop()
        else:
            if s[i] in box:
                print('No')
                return
            else:
                box.append(s[i])
    if len(box) == 0:
        print('Yes')
    else:
        print('No')
