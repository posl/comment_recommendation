def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    d = [0] * n
    for i in range(n):
        d[b[c[i]]] += 1
    print(sum([d[a[i]] for i in range(n)]))
