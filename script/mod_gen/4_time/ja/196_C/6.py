def solve():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            front = str(i)[:len(str(i))//2]
            back = str(i)[len(str(i))//2:]
            if front == back:
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()