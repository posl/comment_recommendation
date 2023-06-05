def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    s = input()
    for i in range(n):
        if s[i] == 'R':
            x[i] += 1
        elif s[i] == 'L':
            x[i] -= 1
    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j] and y[i] == y[j]:
                print('Yes')
                return
    print('No')
main()
