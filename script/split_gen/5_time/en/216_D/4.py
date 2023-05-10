def main():
    n,m = map(int,input().split())
    k = []
    a = []
    for i in range(m):
        k.append(int(input()))
        a.append(list(map(int,input().split())))
    ksum = sum(k)
    if ksum % 2 == 1:
        print("No")
        exit()
    else:
        ksum = int(ksum/2)
    color = []
    for i in range(n):
        color.append(0)
    for i in range(m):
        color[a[i][0]-1] += 1
    for i in range(n):
        if color[i] > 2:
            print("No")
            exit()
    for i in range(n):
        if color[i] == 0:
            print("No")
            exit()
    print("Yes")
