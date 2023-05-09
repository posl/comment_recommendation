def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(tuple(map(int, input().split())))
    l.sort()
    a = l[0][0]
    b = l[0][1]
    for i in range(1, n):
        if l[i][0] <= b:
            if l[i][1] > b:
                b = l[i][1]
        else:
            print(a, b)
            a = l[i][0]
            b = l[i][1]
    print(a, b)
