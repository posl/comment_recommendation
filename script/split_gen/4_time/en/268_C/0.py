def main():
    n = int(input())
    p = [int(i)-1 for i in input().split()]
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i == n-1:
                p[i], p[0] = p[0], p[i]
            else:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)
