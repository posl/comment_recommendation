def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    #print(N, K)
    #print(A)
    #
    # 1. find cycle
    #
    # 1.1. find cycle length
    cycle = []
    visited = [False for _ in range(N)]
    i = 0
    while not visited[i]:
        visited[i] = True
        cycle.append(i)
        i = A[i]
    cycle.append(i)
    cycle_len = len(cycle) - 1
    #print(cycle)
    #print(cycle_len)
    #
    # 1.2. find cycle start
    cycle_start = cycle.index(i)
    #print(cycle_start)
    #
    # 2. find cycle destination
    #
    # 2.1. find cycle destination by cycle length
    cycle_dest = cycle[(K % cycle_len) + cycle_start]
    #print(cycle_dest)
    #
    # 2.2. find cycle destination by cycle start
    if K >= cycle_start:
        cycle_dest = cycle[(K - cycle_start) % cycle_len + cycle_start]
    #print(cycle_dest)
    #
    # 3. output
    print(cycle_dest + 1)
