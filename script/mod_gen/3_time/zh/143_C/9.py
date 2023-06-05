def main():
    #n = int(input())
    #s = input()
    n = 10
    s = 'aabbbbaaca'
    print(s)
    print(n)
    a = s[0]
    count = 1
    for i in range(1,n):
        if s[i] != a:
            a = s[i]
            count = count + 1
    print(count)

if __name__ == '__main__':
    main()