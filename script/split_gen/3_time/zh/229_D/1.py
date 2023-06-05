def main():
    s = input()
    k = int(input())
    n = len(s)
    if k >= n:
        print(n)
        return
    max_x = 0
    cur = 0
    for i in range(n):
        if s[i] == 'X':
            cur += 1
        else:
            if cur > max_x:
                max_x = cur
            cur = 0
    if cur > max_x:
        max_x = cur
    if k == 0:
        print(max_x)
        return
    cur = 0
    for i in range(n):
        if s[i] == '.':
            cur += 1
        else:
            if cur > max_x:
                max_x = cur
            cur = 0
    if cur > max_x:
        max_x = cur
    if k == 1:
        print(max_x + 1)
        return
    cur = 0
    for i in range(n):
        if s[i] == '.':
            cur += 1
        else:
            if cur > max_x:
                max_x = cur
            cur = 0
    if cur > max_x:
        max_x = cur
    print(max_x + k)
