def visible_squares(h,w,x,y):
    #print(h,w,x,y)
    #print(s)
    #print(s[x-1][y-1])
    count = 0
    for i in range(x-1,-1,-1):
        if s[i][y-1] == '#':
            break
        else:
            count += 1
    #print(count)
    for i in range(x,h):
        if s[i][y-1] == '#':
            break
        else:
            count += 1
    #print(count)
    for j in range(y-1,-1,-1):
        if s[x-1][j] == '#':
            break
        else:
            count += 1
    #print(count)
    for j in range(y,w):
        if s[x-1][j] == '#':
            break
        else:
            count += 1
    #print(count)
    return count
h,w,x,y = map(int,input().split())
s = []
for i in range(h):
    s.append(input())
print(visible_squares(h,w,x,y))

if __name__ == '__main__':
    visible_squares()