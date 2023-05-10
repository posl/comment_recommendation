def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        return abs(x-a)
    if n == 1:
        return min(abs(x-a), abs(x-(a+d)))
    if x < a:
        return abs(x-a)
    if x > a + d * (n-1):
        return abs(x-(a+d*(n-1)))
    if (x-a) % d == 0:
        return 0
    else:
        return min(abs(x-(a+d*((x-a)//d))), abs(x-(a+d*((x-a)//d+1))))
