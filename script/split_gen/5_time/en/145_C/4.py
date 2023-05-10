def path_length(path):
    total = 0
    for i in range(len(path)-1):
        total += ((path[i][0]-path[i+1][0])**2 + (path[i][1]-path[i+1][1])**2)**(1/2)
    return total
