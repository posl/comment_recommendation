def main():
    S = input()
    box = set()
    for s in S:
        if s == '(':
            continue
        if s == ')':
            if len(box) == 0:
                print('No')
                return
            box.pop()
        else:
            if s in box:
                print('No')
                return
            box.add(s)
    if len(box) == 0:
        print('Yes')
    else:
        print('No')
