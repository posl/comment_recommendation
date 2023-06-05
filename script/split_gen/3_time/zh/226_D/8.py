def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1,y1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
    x.sort()
    y.sort()
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(3)
    else:
        print(4)
