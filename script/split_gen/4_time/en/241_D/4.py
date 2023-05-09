def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        s = input().split()
        if s[0] == '1':
            a.append(int(s[1]))
            b.append(int(s[1]))
        elif s[0] == '2':
            a.sort()
            k = int(s[2])
            if len(a) < k:
                print(-1)
            else:
                print(a[-k])
        elif s[0] == '3':
            b.sort()
            k = int(s[2])
            if len(b) < k:
                print(-1)
            else:
                print(b[k-1])
    return
main()
