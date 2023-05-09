def main():
    s = input()
    if s[0] == '0':
        print('No')
        return
    for i in range(9):
        if s[i] == '1' and s[i+1] == '1':
            print('Yes')
            return
    print('No')
