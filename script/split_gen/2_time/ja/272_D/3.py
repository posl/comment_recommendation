def main():
    n, m = map(int, input().split())
    if m == 1:
        for i in range(n):
            print(*[abs(i-j) for j in range(n)])
    else:
        for i in range(n):
            print(*[min(abs(i-j), abs(i-j-n), abs(i-j+n)) for j in range(n)])
