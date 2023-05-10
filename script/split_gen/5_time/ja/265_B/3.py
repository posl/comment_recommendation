def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for i in range(m)]
    time = t
    room = 1
    for i in range(n-1):
        time -= a[i]
        if time <= 0:
            print('No')
            return
        if room < xy[0][0]:
            time += xy[0][1]
            room += 1
        else:
            xy.pop(0)
    print('Yes')
