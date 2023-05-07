def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    x = k // n
    y = k % n
    for i in range(n):
        if i < y:
            print(x + 1)
        else:
            print(x)
