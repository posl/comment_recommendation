def main():
    s = input()
    box = set()
    for i in range(len(s)):
        if s[i] == '(':
            continue
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
                box.add(s[i])
    if len(box) != 0:
        print('No')
        return
    print('Yes')
    return
