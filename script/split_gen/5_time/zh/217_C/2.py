def main():
    n = int(raw_input())
    p = map(int, raw_input().split())
    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1
    for i in range(n):
        print q[i],
