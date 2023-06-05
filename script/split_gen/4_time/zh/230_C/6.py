def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    for i in range(p, q+1):
        for j in range(r, s+1):
            if i <= n-a and j <= n-b:
                print('.', end='')
            elif i <= n-a and j >= b-1:
                print('.', end='')
            elif i >= a-1 and j <= n-b:
                print('.', end='')
            elif i >= a-1 and j >= b-1:
                print('.', end='')
            else:
                print('#', end='')
        print()
