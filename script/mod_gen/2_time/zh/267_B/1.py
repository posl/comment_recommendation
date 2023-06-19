def main():
    s = input()
    if s[0] == '0':
        print('No')
        return
    count = 0
    for i in range(1, 10):
        if s[i] == '1':
            count += 1
    if count == 0:
        print('No')
        return
    if count == 1:
        print('Yes')
        return
    for i in range(1, 10):
        if s[i] == '1' and s[i+1] == '0':
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()