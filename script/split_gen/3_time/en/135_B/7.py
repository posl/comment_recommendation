def main():
    N = int(input())
    p = list(map(int, input().split()))
    if p == sorted(p):
        print('YES')
    else:
        ans = 'NO'
        for i in range(N):
            for j in range(i + 1, N):
                p[i], p[j] = p[j], p[i]
                if p == sorted(p):
                    ans = 'YES'
                p[i], p[j] = p[j], p[i]
        print(ans)
