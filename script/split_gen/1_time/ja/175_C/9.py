def main():
    x, k, d = map(int, input().split())
    #print(x, k, d)
    x = abs(x)
    #print(x)
    if x > k * d:
        print(x - k * d)
    else:
        k -= x // d
        x %= d
        if k % 2 == 0:
            print(x)
        else:
            print(d - x)
