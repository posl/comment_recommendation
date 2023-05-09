def main():
    s = input()
    t = input()
    ss = set(s)
    tt = set(t)
    if len(ss) == len(tt):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()