def solve():
    s,t = map(int,input().split())
    count = 0
    for i in range(0,s+1):
        for j in range(0,s+1):
            for k in range(0,s+1):
                if i + j + k <= s and i * j * k <= t:
                    count += 1
    print(count)

if __name__ == '__main__':
    solve()