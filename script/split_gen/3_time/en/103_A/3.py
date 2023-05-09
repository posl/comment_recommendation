def min_cost(tasks):
    return min(abs(tasks[0]-tasks[1])+abs(tasks[1]-tasks[2]), abs(tasks[0]-tasks[2])+abs(tasks[2]-tasks[1]), abs(tasks[0]-tasks[1])+abs(tasks[0]-tasks[2]))
