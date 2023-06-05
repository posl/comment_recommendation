def main():
    n = int(input())
    p = input().split()
    q = [0] * n
    for i in range(n):
        q[int(p[i]) - 1] = str(i + 1)
    print(' '.join(q))
