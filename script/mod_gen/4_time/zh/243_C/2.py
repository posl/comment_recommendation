def main():
    n = int(input())
    x = []
    y = []
    s = []
    for i in range(n):
        t = input().split()
        x.append(int(t[0]))
        y.append(int(t[1]))
    s = input()
    for i in range(n):
        if s[i] == 'R':
            x[i] = x[i] + 1
        else:
            x[i] = x[i] - 1
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] and y[i] == y[j]:
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    main()