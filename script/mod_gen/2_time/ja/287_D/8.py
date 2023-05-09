def main():
    s = input()
    t = input()
    for x in range(len(t)+1):
        s_ = s[x:len(s)-len(t)+x]
        if s_.count('?') + s_.count(t) == len(s_):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()