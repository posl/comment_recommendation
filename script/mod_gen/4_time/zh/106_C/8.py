def main():
    s = input()
    k = int(input())
    a = 0
    b = 0
    c = 0
    for i in range(len(s)):
        if s[i] == '1':
            a += 1
        elif s[i] == '2':
            b += 1
        elif s[i] == '3':
            c += 1
    if k <= a:
        print('1')
    elif k <= a + b:
        print('2')
    else:
        print('3')

if __name__ == '__main__':
    main()