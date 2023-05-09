def solve():
    n = int(input())
    p = list(map(int, input().split()))
    if p == sorted(p):
        print("YES")
        return
    for i in range(n):
        for j in range(i+1, n):
            p[i], p[j] = p[j], p[i]
            if p == sorted(p):
                print("YES")
                return
            p[i], p[j] = p[j], p[i]
    print("NO")
    return
solve()

if __name__ == '__main__':
    solve()