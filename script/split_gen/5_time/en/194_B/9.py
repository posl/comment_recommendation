def main():
    # Get the number of employees
    n = int(input())
    # Get the time taken by each employee to finish the two tasks
    times = []
    for i in range(n):
        times.append(list(map(int, input().split())))
    # Get the minimum time taken to finish the two tasks
    min_time = float('inf')
    for i in range(n):
        for j in range(n):
            if i == j:
                min_time = min(min_time, times[i][0] + times[j][1])
            else:
                min_time = min(min_time, max(times[i][0], times[j][1]))
    # Print the minimum time taken to finish the two tasks
    print(min_time)
