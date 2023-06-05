def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    s = input()
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
    if l == 1 and r == 1:
        print('Yes')
        return
    if l == 1:
        for i in range(n):
            if s[i] == 'L':
                l = i
                break
        for i in range(n):
            if s[i] == 'R':
                r = i
                break
        if x[l] < x[r]:
            print('No')
        else:
            print('Yes')
        return
    if r == 1:
        for i in range(n):
            if s[i] == 'R':
                r = i
                break
        for i in range(n):
            if s[i] == 'L':
                l = i
                break
        if x[r] < x[l]:
            print('No')
        else:
            print('Yes')
        return
    for i in range(n):
        if s[i] == 'L':
            l = i
            break
    for i in range(n - 1, -1, -1):
        if s[i] == 'R':
            r = i
            break
    if x[l] < x[r]:
        print('Yes')
    else:
        print('No')
