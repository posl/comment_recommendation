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
            for j in range(i+1, n):
                if s[j] == 'L':
                    if y[i] == y[j] and x[i] < x[j]:
                        print('Yes')
                        return
    print('No')
