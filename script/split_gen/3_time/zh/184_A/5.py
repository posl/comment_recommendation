def main():
    a = []
    b = []
    for i in range(2):
        a.append(list(map(int, input().split())))
    for i in range(2):
        b.append(list(map(int, input().split())))
    print(a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1])
    print(a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1])
