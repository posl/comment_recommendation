def check(plate, condition):
    cnt = 0
    for i in range(len(condition)):
        if plate[condition[i][0]-1] == 1 and plate[condition[i][1]-1] == 1:
            cnt += 1
    return cnt
