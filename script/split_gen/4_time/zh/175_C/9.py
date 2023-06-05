def main():
    x,k,d = map(int, input().split())
    x = abs(x)
    if x - k*d >= 0:
        print(x - k*d)
    else:
        m = x // d
        if (k-m) % 2 == 0:
            print(x - m*d)
        else:
            print(abs(x - (m+1)*d))
