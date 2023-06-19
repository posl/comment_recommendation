def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    for i in range(p, q+1):
        for j in range(r, s+1):
            if (i+a-j >= 1 and i+a-j <= n) or (i+a+j >= 1 and i+a+j <= n) or (i-a+j >= 1 and i-a+j <= n) or (i-a-j >= 1 and i-a-j <= n):
                print('#', end='')
            else:
                print('.', end='')
        print()
