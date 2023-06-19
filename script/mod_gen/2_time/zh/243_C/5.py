def main():
    n = int(input())
    x = []
    y = []
    s = []
    for i in range(n):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    s = input()
    print(x)
    print(y)
    print(s)
    for i in range(n):
        if s[i] == 'R':
            x[i] += 1
        elif s[i] == 'L':
            x[i] -= 1
    print(x)
    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j] and y[i] == y[j]:
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    main()