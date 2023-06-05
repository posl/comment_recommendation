def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    total = sum(a)
    if total >= x:
        print(n)
    else:
        print(n * (x // total) + sum([1 for i in range(x % total) if sum(a[:i]) > x]))
main()
