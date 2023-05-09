def main():
    x, k = map(int, input().split())
    for i in range(k):
        if x % (10 ** (k - i)) == 0:
            print(x)
            break
        else:
            x = x + (10 ** (k - i))
    else:
        print(x)
