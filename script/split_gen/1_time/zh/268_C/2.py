def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    p = [x-1 for x in p]
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i < n-1:
                p[i], p[i+1] = p[i+1], p[i]
            else:
                p[0], p[i] = p[i], p[0]
    print(ans)
