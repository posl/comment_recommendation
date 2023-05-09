def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p.reverse()
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += p[i]
        else:
            ans += p[i] / 2
    print(int(ans))
