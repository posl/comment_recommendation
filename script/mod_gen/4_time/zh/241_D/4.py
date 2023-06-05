def main():
    q = int(input())
    a = []
    for i in range(q):
        l = list(map(int, input().split()))
        if l[0] == 1:
            a.append(l[1])
        elif l[0] == 2:
            a.sort()
            if len(a) >= l[2]:
                print(a[-l[2]])
            else:
                print(-1)
        elif l[0] == 3:
            a.sort()
            if len(a) >= l[2]:
                print(a[l[2]-1])
            else:
                print(-1)
main()
