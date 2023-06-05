def main():
    n = int(input())
    x = []
    y = []
    s = input()
    for i in range(n):
        t = input().split()
        x.append(int(t[0]))
        y.append(int(t[1]))
    l = 0
    r = 0
    for i in range(n):
        if s[i] == 'L':
            l += 1
        else:
            r += 1
    if l == 0 or r == 0:
        print('No')
        return
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j]:
                if s[i] == 'L' and s[j] == 'R':
                    if y[i] <= y[j]:
                        print('Yes')
                        return
                elif s[i] == 'R' and s[j] == 'L':
                    if y[j] <= y[i]:
                        print('Yes')
                        return
    print('No')

if __name__ == '__main__':
    main()