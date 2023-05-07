def main():
    from sys import stdin
    from collections import defaultdict
    def input():
        return stdin.readline().strip()
    N = int(input())
    ladders = []
    for i in range(N):
        A, B = map(int, input().split())
        ladders.append((A, B))
    # Sort the ladders by their starting point
    ladders.sort()
    # Set of the floors that can be reached
    reached = set()
    # Set of the floors that can be reached by using the ladders that have already been used
    reached_by_used_ladders = set()
    # Set of the floors that can be reached by using the ladders that have not been used
    reached_by_unused_ladders = set()
    # Add the starting floor
    reached.add(1)
    reached_by_unused_ladders.add(1)
    # Iterate through the ladders
    for A, B in ladders:
        # Check if the ladder can be used
        if A in reached_by_unused_ladders or B in reached_by_unused_ladders:
            # Add the floors that can be reached by using this ladder
            reached.add(A)
            reached.add(B)
            reached_by_used_ladders.add(A)
            reached_by_used_ladders.add(B)
            # Remove the floors that can be reached by using the ladders that have not been used
            reached_by_unused_ladders.difference_update(reached_by_used_ladders)
    # Print the answer
    print(max(reached))
