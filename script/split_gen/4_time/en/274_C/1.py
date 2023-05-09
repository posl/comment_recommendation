def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 ** (n + 1))
    for i in range(n):
        b[a[i]] = i + 1
    for i in range(1, 2 ** (n + 1)):
        if i % 2 == 0:
            print(0)
        else:
            print(b[i // 2])
