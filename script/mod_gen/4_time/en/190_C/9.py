def countSatisfiedConditions(dishes, conditions, people):
    satisfiedConditions = 0
    for condition in conditions:
        if dishes[condition[0]-1] and dishes[condition[1]-1]:
            satisfiedConditions += 1
    return satisfiedConditions

if __name__ == '__main__':
    countSatisfiedConditions()