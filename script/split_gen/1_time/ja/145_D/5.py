def main():
    x, y = map(int, input().split())
    if (x+y)%3 != 0:
        print(0)
        exit()
    n = (x+y)//3
    m = (2*x-y)//3
    if n < 0 or m < 0:
        print(0)
        exit()
    print(combination(n, m, 10**9+7))
