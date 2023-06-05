def get_max_satisfied_conditions(N, M, conditions, K, people):
    max_satisfied = 0
    for i in range(2**K):
        satisfied_conditions = 0
        plates = [0]*N
        for j in range(K):
            if (i & (1<<j)) > 0:
                plates[people[j][0]-1] = 1
            else:
                plates[people[j][1]-1] = 1
        for j in range(M):
            if plates[conditions[j][0]-1] == 1 and plates[conditions[j][1]-1] == 1:
                satisfied_conditions += 1
        if max_satisfied < satisfied_conditions:
            max_satisfied = satisfied_conditions
    return max_satisfied
