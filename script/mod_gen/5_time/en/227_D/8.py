def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == k:
        print(1)
        return
    a.sort()
    a.reverse()
    print((n-1 + k - 2) // (k - 1))
main()
