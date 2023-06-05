def main():
    n = int(input())
    a = []
    for i in range(n):
        s = input().split()
        if s[0] == '1':
            a.append(int(s[1]))
        elif s[0] == '2':
            x = int(s[1])
            k = int(s[2])
            b = [i for i in a if i <= x]
            b.sort()
            if len(b) >= k:
                print(b[-k])
            else:
                print(-1)
        elif s[0] == '3':
            x = int(s[1])
            k = int(s[2])
            b = [i for i in a if i >= x]
            b.sort()
            if len(b) >= k:
                print(b[k-1])
            else:
                print(-1)

if __name__ == '__main__':
    main()