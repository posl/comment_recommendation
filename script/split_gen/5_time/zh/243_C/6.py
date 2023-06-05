def main():
    n = int(input())
    x = []
    y = []
    s = []
    for i in range(n):
        x.append(0)
        y.append(0)
        x[i], y[i] = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'R':
            x[i] += 1
        elif s[i] == 'L':
            x[i] -= 1
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] and y[i] == y[j]:
                print('Yes')
                return
    print('No')
    return
