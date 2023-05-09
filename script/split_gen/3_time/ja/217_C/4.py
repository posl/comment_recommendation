def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0 for i in range(n)]
    for i in range(n):
        q[p[i] - 1] = i + 1
    print(*q)
