def main():
    n = int(input())
    a = []
    for _ in range(n):
        s = input().split()
        if s[0] == '1':
            a.append(int(s[1]))
        elif s[0] == '2':
            if len(a) == 0:
                print(-1)
            else:
                b = [x for x in a if x <= int(s[1])]
                if len(b) < int(s[2]):
                    print(-1)
                else:
                    b.sort(reverse=True)
                    print(b[int(s[2])-1])
        elif s[0] == '3':
            if len(a) == 0:
                print(-1)
            else:
                b = [x for x in a if x >= int(s[1])]
                if len(b) < int(s[2]):
                    print(-1)
                else:
                    b.sort()
                    print(b[int(s[2])-1])
