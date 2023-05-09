def problems228_b():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if x & (1 << i):
            ans += 1
    print(ans)

if __name__ == '__main__':
    problems228_b()