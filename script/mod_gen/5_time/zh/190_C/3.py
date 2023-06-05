def count_satisfied_conditions(N, M, conditions, K, persons):
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            satisfied = True
            for k in range(M):
                if i < conditions[k][0] or conditions[k][1] < j:
                    satisfied = False
            for k in range(K):
                if i != persons[k][0] and j != persons[k][1]:
                    satisfied = False
            if satisfied:
                count += 1
    return count

if __name__ == '__main__':
    count_satisfied_conditions()