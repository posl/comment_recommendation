def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    for i in range(p, q + 1):
        for j in range(r, s + 1):
            if (i + j) % 2 == (a + b) % 2:
                print('#', end='')
            else:
                print('.', end='')
        print()
