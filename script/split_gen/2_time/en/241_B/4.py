def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    for b in B:
        while i < N and A[i] < b:
            i += 1
        if i == N or A[i] > b:
            print("No")
            return
        i += 1
    print("Yes")
main()
The problem is to find the shortest path from the starting point to the goal. The graph is given by a 2D array. 0 is a wall and 1 is a free space. The cost of moving from one point to an adjacent point is 1. The cost of moving from one point to a non-adjacent point is 10. The graph is connected. The starting point and the goal are given by two tuples.
The problem is to find the shortest path from the starting point to the goal. The graph is given by a 2D array. 0 is a wall and 1 is a free space. The cost of moving from one point to an adjacent point is 1. The cost of moving from one point to a non-adjacent point is 10. The graph is connected. The starting point and the goal are given by two tuples.
