def problem197_b():
    h,w,x,y = map(int,input().split())
    s = []
    for _ in range(h):
        s.append(input())
    count = 1
    for i in range(1,h):
        if s[x-1][y-1] == '#':
            break
        if x+i <= h and s[x-1+i-1][y-1] == '.':
            count += 1
        else:
            break
    for i in range(1,h):
        if s[x-1][y-1] == '#':
            break
        if x-i >= 1 and s[x-1-i-1][y-1] == '.':
            count += 1
        else:
            break
    for i in range(1,w):
        if s[x-1][y-1] == '#':
            break
        if y+i <= w and s[x-1][y-1+i-1] == '.':
            count += 1
        else:
            break
    for i in range(1,w):
        if s[x-1][y-1] == '#':
            break
        if y-i >= 1 and s[x-1][y-1-i-1] == '.':
            count += 1
        else:
            break
    print(count)

if __name__ == '__main__':
    problem197_b()