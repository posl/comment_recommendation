def count(x, y, r):
    cnt = 0
    for i in range(int(x-r), int(x+r)+1):
        for j in range(int(y-r), int(y+r)+1):
            if (i-x)**2 + (j-y)**2 <= r**2:
                cnt += 1
    return cnt
x, y, r = map(float, input().split())
print(count(x, y, r))
