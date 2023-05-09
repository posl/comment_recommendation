def countHappyPeople(people):
    happyPeople = 0
    for i in range(len(people)-1):
        if people[i] == people[i+1]:
            happyPeople += 1
    return happyPeople
