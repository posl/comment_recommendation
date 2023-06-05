def solve():
    n = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if n == i * j:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    solve()