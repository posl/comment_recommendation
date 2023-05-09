def main():
    n, q = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = i + 1
    for i in range(q):
        x = int(input())
        for j in range(n):
            if a[j] == x:
                if j != n - 1:
                    a[j], a[j + 1] = a[j + 1], a[j]
                else:
                    a[j], a[j - 1] = a[j - 1], a[j]
                break
    for i in range(n):
        print(a[i], end = " ")
