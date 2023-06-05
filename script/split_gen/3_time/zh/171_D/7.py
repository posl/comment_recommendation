def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = [0 for _ in range(q)]
    c = [0 for _ in range(q)]
    for i in range(q):
        b[i], c[i] = map(int, input().split())
    sum = 0
    for i in range(n):
        sum += a[i]
    for i in range(q):
        sum += (c[i] - b[i]) * a.count(b[i])
        print(sum)
        sum = 0
