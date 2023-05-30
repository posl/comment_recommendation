def main():
    s = input()
    for i in range(0, len(s), 2):
        if s[i] == 'L':
            print('No')
            exit()
    for i in range(1, len(s), 2):
        if s[i] == 'R':
            print('No')
            exit()
    print('Yes')
main()
