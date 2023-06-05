def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * n
    for i in range(1, n):
        c[a[i] - 1] += 1
    for i in range(n):
        print(c[i])
main()
