def find_second_highest_mountain(mountain_list):
    highest = 0
    second_highest = 0
    highest_mountain = ''
    second_highest_mountain = ''
    for mountain in mountain_list:
        if mountain[1] > highest:
            second_highest = highest
            second_highest_mountain = highest_mountain
            highest = mountain[1]
            highest_mountain = mountain[0]
        elif mountain[1] > second_highest:
            second_highest = mountain[1]
            second_highest_mountain = mountain[0]
    return second_highest_mountain
