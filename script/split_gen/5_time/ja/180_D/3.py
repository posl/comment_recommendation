def main():
    x, y, a, b = map(int, input().split())
    cnt = 0
    while a*x < x+b and a*x < y:
        x *= a
        cnt += 1
    cnt += (y-1-x)//b
    print(cnt)
