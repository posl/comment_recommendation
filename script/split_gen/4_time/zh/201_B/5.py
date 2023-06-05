def get_second_highest_mountain_name(mountains):
    highest_mountain = 0
    second_highest_mountain = 0
    for mountain in mountains:
        if mountain[1] > highest_mountain:
            second_highest_mountain = highest_mountain
            highest_mountain = mountain[1]
        elif mountain[1] > second_highest_mountain:
            second_highest_mountain = mountain[1]
    for mountain in mountains:
        if mountain[1] == second_highest_mountain:
            return mountain[0]
