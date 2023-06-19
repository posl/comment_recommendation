def main():
    s = input()
    if s[0] == '0':
        print('No')
    else:
        for i in range(1, 10):
            if s[i] == '0':
                print('Yes')
                return
        print('No')
