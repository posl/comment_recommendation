def solve():
    a, b = map(int, input().split())
    if a * 1 <= b <= a * 6:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()