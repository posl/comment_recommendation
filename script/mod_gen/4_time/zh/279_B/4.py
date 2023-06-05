def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    for i in range(len_s-len_t+1):
        if s[i:i+len_t] == t:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()