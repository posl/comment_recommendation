def main():
    n,k = map(int,input().split())
    s = input()
    s = list(s)
    for i in range(k):
        for j in range(n-1):
            if s[j] == '0' and s[j+1] == '1':
                s[j] = '1'
                s[j+1] = '0'
    print(s.count('1'))

if __name__ == '__main__':
    main()