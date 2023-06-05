def get_second_highest_mountain(mountains):
    highest_mountain = [0, 0]
    second_highest_mountain = [0, 0]
    for mountain in mountains:
        if mountain[1] > highest_mountain[1]:
            second_highest_mountain = highest_mountain
            highest_mountain = mountain
        elif mountain[1] > second_highest_mountain[1]:
            second_highest_mountain = mountain
    return second_highest_mountain[0]

if __name__ == '__main__':
    get_second_highest_mountain()