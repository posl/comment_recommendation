def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print('No')
    else:
        for i in range(len(s) - len(t) + 1):
            if s[i:i + len(t)] == t:
                print('Yes')
                exit()
        print('No')

if __name__ == '__main__':
    main()