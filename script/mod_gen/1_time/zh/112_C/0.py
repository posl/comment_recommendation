def get_center(x1,y1,h1,x2,y2,h2,x3,y3,h3):
    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1
    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1
    if h1 == h2:
        h4 = h3
    elif h1 == h3:
        h4 = h2
    else:
        h4 = h1
    return x4,y4,h4
N = int(input())
x = []
y = []
h = []
for i in range(N):
    x1,y1,h1 = map(int, input().split())
    x.append(x1)
    y.append(y1)
    h.append(h1)
for j in range(N):
    if h[j] > 0:
        x4,y4,h4 = get_center(x[0],y[0],h[0],x[1],y[1],h[1],x[j],y[j],h[j])
        break
print(x4,y4,h4)

if __name__ == '__main__':
    get_center()