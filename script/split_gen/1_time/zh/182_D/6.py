def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    s[0] = a[0]
    for i in range(1, n):
        s[i] = s[i-1] + a[i]
    print(max(s))
main()
