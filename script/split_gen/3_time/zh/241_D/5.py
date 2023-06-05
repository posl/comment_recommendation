def main():
    n = int(input())
    a = []
    for i in range(n):
        x = input().split()
        if x[0] == '1':
            a.append(int(x[1]))
        elif x[0] == '2':
            a.sort()
            if len(a) >= int(x[2]):
                print(a[-int(x[2])])
            else:
                print(-1)
        elif x[0] == '3':
            a.sort()
            if len(a) >= int(x[2]):
                print(a[int(x[2])-1])
            else:
                print(-1)
