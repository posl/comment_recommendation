def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] >= 'a' and s[i] <= 'z':
                continue
            else:
                print('No')
                return
        else:
            if s[i] >= 'A' and s[i] <= 'Z':
                continue
            else:
                print('No')
                return
    print('Yes')
    return
main()
