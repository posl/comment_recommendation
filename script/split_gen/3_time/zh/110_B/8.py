def main():
    n, m, x, y = map(int, input().split())
    xx = list(map(int, input().split()))
    yy = list(map(int, input().split()))
    xx.append(x)
    yy.append(y)
    xx.sort()
    yy.sort()
    if xx[-1] < yy[0]:
        print('No War')
    else:
        print('War')
