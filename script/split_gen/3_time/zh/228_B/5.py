def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    b = [0] * n
    for i in range(n):
        b[a[i]] += 1
    if b[x - 1] == 0:
        print(0)
        return
    b[x - 1] = 0
    for i in range(n):
        if b[i] > 0:
            print(b[i] + 1)
