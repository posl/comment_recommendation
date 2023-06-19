def main():
    n, x = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        if (b - a) <= x:
            pass
        else:
            print('No')
            return
    print('Yes')
