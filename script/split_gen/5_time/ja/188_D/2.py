def calc_cost(services, c):
    cost = 0
    for service in services:
        cost += service[2]
    cost += c
    return cost
