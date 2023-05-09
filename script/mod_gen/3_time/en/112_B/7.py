def solve():
    N, T = map(int, input().split())
    min_cost = 1001
    for i in range(N):
        c, t = map(int, input().split())
        if t <= T:
            min_cost = min(min_cost, c)
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)
solve()
I solved this problem by using a greedy algorithm. If the time is less than or equal to the time limit, then check if the cost is less than the minimum cost. If it is, update the minimum cost. If the minimum cost is not updated, then there is no route that takes not longer than time T. In this case, print TLE instead.

if __name__ == '__main__':
    solve()