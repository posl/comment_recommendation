def main():
    n = int(input())
    s = input()
    l = len(s)
    if n == 1:
        print(s)
        return
    s = list(s)
    cnt = 0
    for i in range(l):
        if s[i] == '"':
            cnt += 1
        elif s[i] == ',' and cnt % 2 == 1:
            s[i] = '.'
    print(''.join(s))

if __name__ == '__main__':
    main()