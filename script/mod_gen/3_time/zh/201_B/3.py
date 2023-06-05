def get_second_highest_mountain_name(mountain_list):
    highest_mountain = mountain_list[0]
    second_highest_mountain = mountain_list[0]
    for mountain in mountain_list:
        if mountain[1] > highest_mountain[1]:
            second_highest_mountain = highest_mountain
            highest_mountain = mountain
        elif mountain[1] > second_highest_mountain[1]:
            second_highest_mountain = mountain
    return second_highest_mountain[0]

if __name__ == '__main__':
    get_second_highest_mountain_name()