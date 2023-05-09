def solve():
    # T
    T = int(input())
    for _ in range(T):
        # N
        N = int(input())
        # A_1 A_2 ... A_N
        A = list(map(int, input().split()))
        # 出力
        print(len([a for a in A if a % 2 == 1]))

if __name__ == '__main__':
    solve()