def getDistance(start, goal, n):
    if start == goal:
        return 0
    if start > goal:
        start, goal = goal, start
    if start == 1 and goal == n:
        return 1
    if start == 1:
        return goal - start
    if goal == n:
        return goal - start
    return min(goal - start, start + n - goal)
