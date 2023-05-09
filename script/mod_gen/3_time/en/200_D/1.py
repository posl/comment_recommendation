def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 200 == 0:
                print("Yes")
                print(1, i+1)
                print(1, j+1)
                return
    print("No")
    return

if __name__ == '__main__':
    solve()