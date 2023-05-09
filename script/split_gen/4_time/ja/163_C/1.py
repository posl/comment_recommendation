def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(1, n):
        ans[a[i-1]-1] += 1
    for i in ans:
        print(i)
