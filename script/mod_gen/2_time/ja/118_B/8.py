def solve():
    N, M = map(int, input().split())
    foods = [0] * M
    for _ in range(N):
        foods += map(int, input().split())
    print(len(set(foods)))

if __name__ == '__main__':
    solve()