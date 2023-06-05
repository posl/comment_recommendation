def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, k)
    # print(a)
    a.sort()
    # print(a)
    ans = k // n
    b = k % n
    # print(ans)
    # print(b)
    for i in range(n):
        if a[i] <= b:
            print(ans+1)
        else:
            print(ans)
