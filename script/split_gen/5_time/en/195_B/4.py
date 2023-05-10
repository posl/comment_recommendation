def main():
    a,b,w = map(int, input().split())
    w *= 1000
    mn = 1000000000
    mx = 0
    for i in range(1, w+1):
        if a*i <= w and w <= b*i:
            mn = min(mn, i)
            mx = max(mx, i)
    if mn == 1000000000:
        print('UNSATISFIABLE')
    else:
        print(mn, mx)
