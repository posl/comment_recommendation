def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = list(map(int, input().split()))
        if sum([a[j] * b[j] for j in range(m)]) + c > 0:
            count += 1
    print(count)
