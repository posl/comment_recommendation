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
            b = [t for t in a if t <= x]
            if len(b) < k:
                print(-1)
            else:
                b.sort(reverse=True)
                print(b[k-1])
        else:
            x = int(s[1])
            k = int(s[2])
            b = [t for t in a if t >= x]
            if len(b) < k:
                print(-1)
            else:
                b.sort()
                print(b[k-1])
main()
