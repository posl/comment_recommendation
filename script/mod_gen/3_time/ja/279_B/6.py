def main():
    s = input()
    t = input()
    #print(s)
    #print(t)
    if len(s) < len(t):
        print('No')
    else:
        for i in range(len(s)):
            if s[i] == t[0]:
                #print(s[i:i+len(t)])
                if s[i:i+len(t)] == t:
                    print('Yes')
                    break
        else:
            print('No')

if __name__ == '__main__':
    main()