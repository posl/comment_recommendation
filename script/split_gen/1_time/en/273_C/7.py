def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = [0] * n
    x = 0
    for i in range(n):
        if a[i] != a[i+1]:
            ans[x] = i + 1
            x = 0
        else:
            x += 1
    for i in range(n):
        print(ans[i])
