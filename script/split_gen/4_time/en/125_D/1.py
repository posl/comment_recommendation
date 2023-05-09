def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        print(sum(map(abs, a)))
    else:
        print(sum(map(abs, a)) - 2 * min(abs(a[0]), abs(a[-1])))
