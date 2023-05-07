def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = k // n
    mod = k % n
    for i in range(n):
        if i < mod:
            print(ans + 1)
        else:
            print(ans)
