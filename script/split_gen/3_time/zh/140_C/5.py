def main():
    n = int(input())
    b = list(map(int, input().split()))
    b.append(0)
    a = [0 for i in range(n)]
    a[0] = b[0]
    for i in range(1, n):
        a[i] = min(b[i - 1], b[i])
    print(sum(a))
