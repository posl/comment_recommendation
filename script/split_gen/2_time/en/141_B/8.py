def main():
    s = input()
    if s[0] == 'L' or s[1] == 'L':
        print('No')
        return
    for i in range(2, len(s), 2):
        if s[i] == 'L' or s[i + 1] == 'R':
            print('No')
            return
    print('Yes')
