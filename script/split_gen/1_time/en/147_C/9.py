def check_honesty(people, i, honest_list):
    if i in honest_list:
        return True
    else:
        for j in range(len(people[i])):
            if people[i][j][1] == 1:
                if not check_honesty(people, people[i][j][0] - 1, honest_list):
                    return False
            else:
                if check_honesty(people, people[i][j][0] - 1, honest_list):
                    return False
        return True
