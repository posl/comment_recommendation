def main():
    n, k, q = map(int, input().split())
    a = [0] * n
    for i in range(q):
        a[int(input()) - 1] += 1
    for i in range(n):
        if k - (q - a[i]) > 0:
            print("Yes")
        else:
            print("No")
