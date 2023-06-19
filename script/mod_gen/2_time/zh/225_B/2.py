def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    AB = sorted(AB, key=lambda x: x[0])
    # print(AB)
    if AB[0][1] == N:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()