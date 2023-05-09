def main():
    n = int(input())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
    l = sorted(l, key=lambda x: x[1:])
    ans = 1
    for i in range(n-1):
        if l[i] != l[i+1]:
            ans += 1
    print(ans)
