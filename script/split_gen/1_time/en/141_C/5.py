def main():
    n, k, q = map(int, input().split())
    p = [k - q] * n
    for _ in range(q):
        a = int(input())
        p[a-1] += 1
    for i in range(n):
        if p[i] > 0:
            print("Yes")
        else:
            print("No")
