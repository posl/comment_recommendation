def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [0] * (max(a) + 1)
    d = [0] * (max(b) + 1)
    for i in range(n):
        c[a[i]] += 1
        d[b[i]] += 1
    print(sum([min(c[i], d[i]) for i in range(len(c))]))
    print(sum([min(c[i], d[i]) for i in range(len(c))]) - sum([1 for i in range(n) if a[i] == b[i]]))
main()
