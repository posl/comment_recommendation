def main():
    n = int(input())
    s = [0] * n
    t = [0] * n
    for i in range(n):
        s[i], t[i] = input().split()
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j] or t[i] == t[j]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()