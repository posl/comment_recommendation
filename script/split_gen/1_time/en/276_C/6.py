def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[i] = p.index(i + 1) + 1
    q = sorted(q)
    for i in range(n):
        print(q[i], end=" ")
