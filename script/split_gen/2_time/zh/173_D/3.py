def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    a.append(a[1])
    ans = sum(a)
    for i in range(n):
        ans -= min(a[i], a[i+1], a[i+2])
    print(ans)
