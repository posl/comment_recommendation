def min_cost(x):
    total_cost = 0
    for i in range(len(x)):
        total_cost += (x[i] - sum(x)/len(x))**2
    return total_cost

if __name__ == '__main__':
    min_cost()