def main():
    n, q = map(int, input().split())
    a = list(range(1, n+1))
    for i in range(q):
        x = int(input())
        a[i%n], a[(i+1)%n] = a[(i+1)%n], a[i%n]
    print(*a)
