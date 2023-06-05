def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    x = [False] * (n+1)
    x[0] = True
    y = [False] * (n+1)
    for i in range(n):
        if s[i] == 'AND':
            y[i+1] = y[i] and x[i]
        else:
            y[i+1] = y[i] or x[i]
    print(2 ** (n - y.count(False)))
