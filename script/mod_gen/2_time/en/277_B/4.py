def main():
    n = int(input())
    s = [input() for i in range(n)]
    if len(set(s)) == n and all(s[i][0] in 'HDCS' for i in range(n)) and all(s[i][1] in 'A23456789TJQK' for i in range(n)):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()