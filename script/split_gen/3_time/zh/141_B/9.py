def main():
    s = input()
    if len(s) % 2 == 0:
        for i in range(1, len(s), 2):
            if s[i] == 'R':
                print('No')
                return
        for i in range(0, len(s), 2):
            if s[i] == 'L':
                print('No')
                return
    else:
        for i in range(0, len(s), 2):
            if s[i] == 'R':
                print('No')
                return
        for i in range(1, len(s), 2):
            if s[i] == 'L':
                print('No')
                return
    print('Yes')
