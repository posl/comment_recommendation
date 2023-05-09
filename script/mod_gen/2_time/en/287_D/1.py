def main():
    s = input()
    t = input()
    for i in range(len(t) + 1):
        if s[:i].replace('?', 'a') + s[-(len(t) - i):].replace('?', 'a') == t:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()