def solve():
    n, x = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        if (x-a)%b == 0:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    solve()