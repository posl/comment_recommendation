def main():
    x, k, d = map(int, input().split())
    if x<0:
        x = -x
    if x//d >= k:
        print(x-d*k)
        return
    x = x%d
    if (k-(x//d))%2 == 0:
        print(x%d)
    else:
        print(d-x%d)
