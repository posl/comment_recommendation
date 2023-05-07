def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    num = k // n
    mod = k % n
    for i in range(n):
        ans[i] += num
    for i in range(mod):
        ans[i] += 1
    for i in range(n):
        print(ans[i])
