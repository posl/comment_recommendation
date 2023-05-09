def main():
    s = input()
    s = s.replace('(','')
    s = s.replace(')','')
    s = s.replace('a','')
    s = s.replace('b','')
    s = s.replace('c','')
    if len(s) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()