def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    a = sorted(a)
    b = sorted(b)
    c = sorted(c)
    count = 0
    for i in range(n):
        count += sum([1 for j in range(n) if a[i] == b[c[j]]])
    print(count)
