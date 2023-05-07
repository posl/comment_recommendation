def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for i in range(q)]
    b = [1]
    for i in range(n):
        b.append(b[-1] * 2)
    for i in range(q):
        c = 0
        for j in range(n):
            if k[i] > a[j]:
                c += 1
        print(b[c] + k[i] - 1)
