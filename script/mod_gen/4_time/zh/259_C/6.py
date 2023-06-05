def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        if s + s[-1] == t:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()