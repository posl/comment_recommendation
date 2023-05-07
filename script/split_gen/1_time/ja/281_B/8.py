def main():
    S = input()
    tmp = ''
    for s in S:
        if s.isupper():
            if len(tmp) == 6 and tmp.isdigit() and 100000 <= int(tmp) <= 999999:
                tmp = ''
            else:
                break
        else:
            tmp += s
    else:
        if len(tmp) == 6 and tmp.isdigit() and 100000 <= int(tmp) <= 999999:
            print('Yes')
        else:
            print('No')
        return
    print('No')
