def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(len(s)-1):
        tmp = list(s)
        tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
        if ''.join(tmp) == t:
            print('Yes')
            return
    print('No')
