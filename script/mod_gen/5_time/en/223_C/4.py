def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for i in range(N)]
    s = 0
    for i in range(N):
        s += AB[i][0]/AB[i][1]
    s /= 2
    t = 0
    for i in range(N):
        t += AB[i][0]/AB[i][1]
        if t>=s:
            print(s)
            break
        else:
            continue

if __name__ == '__main__':
    solve()