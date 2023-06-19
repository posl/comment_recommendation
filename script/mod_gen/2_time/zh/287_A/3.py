def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    count = 0
    for i in range(n):
        if s[i] == "For":
            count += 1
    if count > n/2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()