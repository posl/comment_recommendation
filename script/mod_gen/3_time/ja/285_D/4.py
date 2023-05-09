def main():
    n = int(input())
    s = [0] * n
    t = [0] * n
    for i in range(n):
        s[i], t[i] = input().split()
    for i in range(n):
        for j in range(n):
            if i != j and s[i] == s[j]:
                print('No')
                return
    for i in range(n):
        for j in range(n):
            if i != j and s[i] == t[j]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()