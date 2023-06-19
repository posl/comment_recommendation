def check_collision(people):
    for i in range(len(people)):
        for j in range(i+1, len(people)):
            if people[i][0] == people[j][0] and people[i][1] == people[j][1]:
                return True
    return False

if __name__ == '__main__':
    check_collision()